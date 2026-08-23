import crypto from "crypto";
import clientPromise from "../lib/db.js";

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Credentials", "true");
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, OPTIONS, POST, PUT, DELETE");
  res.setHeader("Access-Control-Allow-Headers", "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  if (req.method !== "POST") {
    return res.status(405).send("Method Not Allowed");
  }

  const { name, email, phone, amount, lastName, address, cart, discount, subtotal } = req.body || {};

  const key         = process.env.PAYU_KEY;
  const salt        = process.env.PAYU_SALT;
  const txnid       = "WRX" + Date.now();
  const productinfo = "WARAX Gaming Order";

  const formattedAmount = parseFloat(amount || 0).toFixed(2);
  const formattedPhone  = String(phone || "").replace(/\D/g, "").slice(-10);
  const formattedName   = (name || "Customer").trim();

  // PayU Hash calculation (SHA-512)
  const hashString =
    key + "|" + txnid + "|" + formattedAmount + "|" +
    productinfo + "|" + formattedName + "|" + email +
    "|||||||||||" + salt;

  const hash = crypto.createHash("sha512").update(hashString).digest("hex");

  // Save pending order to MongoDB
  try {
    const client = await clientPromise;
    const db = client.db("waraxgaming");
    await db.collection("orders").insertOne({
      txnid,
      name: formattedName,
      lastName,
      email,
      phone     : formattedPhone,
      amount    : formattedAmount,
      address,
      cart,
      discount,
      subtotal,
      status    : "pending",
      createdAt : new Date()
    });
  } catch(e) {
    console.error("DB error:", e);
  }

  const host = req.headers.host || "waraxgaming-backend.vercel.app";
  const protocol = host.includes("localhost") ? "http" : "https";

  return res.status(200).json({
    success     : true,
    key,
    txnid,
    productinfo,
    amount      : formattedAmount,
    hash,
    surl        : `${protocol}://${host}/api/success`,
    furl        : "https://waraxgaming.store/payment-failed.html"
  });
}
