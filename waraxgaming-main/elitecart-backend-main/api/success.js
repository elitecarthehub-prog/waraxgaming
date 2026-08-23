import crypto from "crypto";
import clientPromise from "../lib/db.js";

export const config = { api: { bodyParser: true } };

export default async function handler(req, res) {
  const frontendUrl = process.env.FRONTEND_URL || "https://waraxgaming.store";

  try {
    if (req.method !== "POST") return res.status(405).send("Method Not Allowed");
    const body = req.body || {};
    const { status, firstname, amount, txnid, key, productinfo, email, hash } = body;
    if (!status || !txnid) return res.status(400).send("Invalid PayU response");

    const salt = process.env.PAYU_SALT;
    if (!salt) return res.status(500).send("PAYU_SALT missing");

    // PayU CORRECT reverse hash format
    // salt|status|udf10|udf9|udf8|udf7|udf6|udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key
    const hashString =
      salt + "|" + status +
      "|||||||||||" +
      email + "|" + firstname + "|" + productinfo + "|" +
      amount + "|" + txnid + "|" + key;

    const generatedHash = crypto.createHash("sha512").update(hashString).digest("hex");

    if (generatedHash === hash) {
      const client = await clientPromise;
      const db = client.db("waraxgaming");

      if (status === "success") {
        await db.collection("orders").updateOne(
          { txnid },
          { $set: { status: "paid", paidAt: new Date() } }
        );
        return res.redirect(302, `${frontendUrl}/checkout.html?status=success`);
      } else {
        await db.collection("orders").updateOne(
          { txnid },
          { $set: { status: "failed", failedAt: new Date() } }
        );
        return res.redirect(302, `${frontendUrl}/payment-failed.html`);
      }
    }

    console.warn("PayU hash mismatch on success callback. Calculated:", generatedHash, "Received:", hash);
    return res.redirect(302, `${frontendUrl}/payment-failed.html`);
  } catch (err) {
    console.error("SUCCESS API ERROR:", err);
    return res.redirect(302, `${frontendUrl}/payment-failed.html`);
  }
}
