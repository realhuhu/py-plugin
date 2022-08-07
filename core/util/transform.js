import fetch from "node-fetch";

export async function imageUrlToBuffer(url) {
  return Buffer.from(await fetch(url).then(res => res.arrayBuffer()));
}