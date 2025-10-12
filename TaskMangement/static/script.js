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
setInProgress = (id) => {
  formData = new FormData();
  formData.append("id", id);
  formData.append("subject", "set_in_progress");
  formData.append("csrfmiddlewaretoken", csrfToken);
  upload(formData);
};
setInCompleated = (id) => {
  formData = new FormData();
  formData.append("id", id);
  formData.append("subject", "set_in_compleated");
  formData.append("csrfmiddlewaretoken", csrfToken);
  upload(formData);
}
remove = (id) => {
  formData = new FormData();
  formData.append("id", id);
  formData.append("subject", "remove");
  formData.append("csrfmiddlewaretoken", csrfToken);
  upload(formData);
}
async function addComment() {
  let subject = prompt("Kommentar hinzufügen:");
  if (subject === null || subject.trim() === "") {
    return; // Abbrechen, wenn kein Name eingegeben wurde
  }
  let description = prompt("Beschreibung hinzufügen (optional):");
  if (description === null || description.trim() === "") {
    description = ""; // Beschreibung kann leer sein
  }
  formData = new FormData();
  formData.append("subject", subject);
  formData.append("description", description); // Beschreibung kann leer sein
  formData.append("csrfmiddlewaretoken", csrfToken);
  upload(formData);
}
async function upload(formData) {
  await fetch("/management/", {
    method: "POST",
    body: formData,
  }).then(() => {
    reload();
  });
}
function reload() {
  window.location.reload();
}
