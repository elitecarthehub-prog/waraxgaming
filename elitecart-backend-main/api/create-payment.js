import crypto from "crypto";
import clientPromise from "../lib/db.js";

export default async function handler(req, res) {
  // CORS configuration
  const allowedOrigins = [
    "https://waraxgaming.store",
    "https://waraxgaming.vercel.app"
  ];
  const origin = req.headers.origin;
  if (origin && (allowedOrigins.includes(origin) || origin.startsWith("http://localhost:") || origin.startsWith("http://127.0.0.1:"))) {
    res.setHeader("Access-Control-Allow-Origin", origin);
  } else {
    res.setHeader("Access-Control-Allow-Origin", "https://waraxgaming.store");
  }
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") return res.status(200).end();
  if (req.method !== "POST") return res.status(405).send("Method Not Allowed");

  const { name, email, phone, amount, lastName, address, cart, discount, subtotal } = req.body;
  const key         = process.env.PAYU_KEY;
  const salt        = process.env.PAYU_SALT;
  const txnid       = "WX" + Date.now();
  const productinfo = "Warax Gaming Order";
  const formattedAmount = parseFloat(amount).toFixed(2);
  const formattedPhone  = String(phone).replace(/\D/g, "").slice(-10);

  const hashString =
    key + "|" + txnid + "|" + formattedAmount + "|" +
    productinfo + "|" + name + "|" + email +
    "|||||||||||" + salt;
  const hash = crypto.createHash("sha512").update(hashString).digest("hex");

  try {
    const client = await clientPromise;
    const db = client.db("waraxgaming");
    await db.collection("orders").insertOne({
      txnid, name, email,
      phone     : formattedPhone,
      amount    : formattedAmount,
      lastName, address, cart, discount, subtotal,
      status    : "pending",
      createdAt : new Date()
    });
  } catch(e) {
    console.error("DB error:", e);
  }

  const backendUrl = process.env.BACKEND_URL || "https://waraxgaming.vercel.app";

  return res.status(200).json({
    success     : true,
    key, txnid,
    productinfo,
    amount      : formattedAmount,
    hash,
    surl        : `${backendUrl}/api/success`,
    furl        : `${backendUrl}/api/success`
  });
}
