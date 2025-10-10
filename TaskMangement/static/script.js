let headline;
let description;
let formData;
function addTask() {
  headline = prompt("Neues Element hinzufügen:");
  if (headline === null || headline.trim() === "") {
    return; // Abbrechen, wenn kein Name eingegeben wurde
  }
  description = prompt("Beschreibung hinzufügen:");
  if (description === null || description.trim() === "") {
    return; // Abbrechen, wenn keine Beschreibung eingegeben wurde
  }
  formData = new FormData();
  formData.append("headline", headline);
  formData.append("description", description);
  formData.append("subject", "add");
  formData.append("csrfmiddlewaretoken", csrfToken);
  upload(formData);
}
function upload(formData) {
  fetch("/management/", {
    method: "POST",
    body: formData,
  }).then(() => {
    reload();
  });
}
function reload() {
  window.location.reload();
}
