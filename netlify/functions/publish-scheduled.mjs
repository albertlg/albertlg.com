// Scheduled function: publishes future-dated posts once their date arrives.
// The list comes from the build of the current deploy (netlify/scheduled-posts.mjs): those posts
// were still in the future then, so they are not on the site yet. When one is due, call the
// build hook so Netlify builds the site again and publishes it. The new build no longer lists
// that post, so the function stops triggering by itself.
import { dates } from "../generated/scheduled-posts.mjs";

export default async () => {
  const now = Date.now();
  const due = dates.filter((date) => Date.parse(date) <= now);
  if (due.length === 0) {
    console.log(`Nothing to publish (${dates.length} scheduled).`);
    return;
  }
  const hook = process.env.BUILD_HOOK_URL;
  if (!hook) {
    console.error("BUILD_HOOK_URL is not set, so the site cannot be rebuilt.");
    return;
  }
  const response = await fetch(hook, { method: "POST", body: "{}" });
  console.log(`Due: ${due.join(", ")}. Build hook answered ${response.status}.`);
};

// Every 30 minutes (UTC).
export const config = { schedule: "*/30 * * * *" };
