document.getElementById("fillBtn").addEventListener("click", () => {
  let jsonText = document.getElementById("jsonInput").value;

  let data;
  try {
    data = JSON.parse(jsonText);
  } catch (e) {
    alert("Invalid JSON");
    return;
  }

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, {
      action: "fillForm",
      payload: data
    });
  });
});


document.getElementById("submitPopupBtn").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, {
      action: "submitForm"
    });
  });
});

