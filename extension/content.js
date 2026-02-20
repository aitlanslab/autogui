console.log("ChatGPT watcher loaded");

let intervalId = null;
let triggered = false;

function isValidJSON(text) {
  try {
    const parsed = JSON.parse(text);
    return typeof parsed === "object" && parsed !== null;
  } catch (e) {
    console.log("JSON parse error:", e);
    console.log("Full text:", text);
    return false;
  }
}

function checkParagraph() {
  // Stop if already handled
  if (triggered) return;

  if (!window.location.href.includes("chatgpt.com")) {
    return;
  }

  //const codes = document.querySelectorAll("code");
  const codes=document.getElementById("code-block-viewer")
  if (codes.length === 0) return;
  const text = codes.innerText.trim();

  if (text !== "" && isValidJSON(text)) {
    triggered = true;

    // stop the interval immediately
    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
    }

    alert("Valid JSON detected:\n" + text);

    navigator.clipboard.writeText(text)
      .then(() => {
        console.log("JSON copied to clipboard");
        window.location.reload();
      })
      .catch(err => console.error("Failed to copy:", err));
  }
}

// start polling
intervalId = setInterval(checkParagraph, 1000);
