import crypto from "crypto";
import clientPromise from "../lib/db.js";

export const config = { api: { bodyParser: true } };

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Credentials", "true");
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, OPTIONS, POST");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  try {
    if (req.method !== "POST") return res.status(405).send("Method Not Allowed");

    const body = req.body || {};
    const { status, firstname, amount, txnid, key, productinfo, email, hash } = body;

    if (!status || !txnid) return res.status(400).send("Invalid PayU response");

    const salt = process.env.PAYU_SALT;
    if (!salt) return res.status(500).send("PAYU_SALT missing");

    // PayU Reverse Hash Verification String:
    // salt|status|||||||||||email|firstname|productinfo|amount|txnid|key
    const hashString =
      salt + "|" + status +
      "|||||||||||" +
      email + "|" + firstname + "|" + productinfo + "|" +
      amount + "|" + txnid + "|" + key;

    const generatedHash = crypto.createHash("sha512").update(hashString).digest("hex");

    if (generatedHash === hash && status === "success") {
      try {
        const client = await clientPromise;
        const db = client.db("waraxgaming");
        await db.collection("orders").updateOne(
          { txnid },
          { $set: { status: "paid", paidAt: new Date() } }
        );
      } catch (dbErr) {
        console.error("DB update error:", dbErr);
      }
      return res.redirect(302, "https://waraxgaming.store/checkout.html?status=success");
    }

    return res.redirect(302, "https://waraxgaming.store/checkout.html?status=failure");

  } catch (err) {
    console.error("SUCCESS API ERROR:", err);
    return res.redirect(302, "https://waraxgaming.store/checkout.html?status=failure");
  }
}
