// checkFirstData() prüft alle Eingaben des Nutzers auf Vollständigkeit und gibt dem Nutzer eine Rückmeldung, wenn
// Daten fehlen oder nicht den Vorgaben entsprechen.

function checkFirstData(){

    let jguVorname = document.getElementById("jgu-vorname");
    let jguNachname = document.getElementById("jgu-nachname");
    let jguTopc = document.getElementById("jgu-topic");
    let jguPassword = document.getElementById("jgu-password");
    let jguPasswordNew = document.getElementById("jgu-password-new");
    let jguSubmitter = document.getElementById("jgu-submit");
    let jguNotification = document.getElementById("jgu-notification");

    let errorCounter = 0;
    let errorMessage = "";

    if (jguVorname.value.length < 3 || jguNachname.value.length < 3){
        errorCounter++;
        errorMessage = "Ihr Vor- oder Nachname ist zu kurz."
    } else if (jguPassword.value.length < 4){
        errorCounter++;
        errorMessage = "Ihr Passwort ist zu kurz."
    } else {
        if (jguPasswordNew.value.length !== 0){
            if (jguPasswordNew.value.length < 4){
                errorCounter++;
                errorMessage = "Ihr neues Passwort ist zu kurz."
            } else if (jguPassword.value == jguPasswordNew.value){
                errorCounter++;
                errorMessage = "Ihr neues und Ihr altes Passwort dürfen nicht gleich sein."
            }
        }
    }

    if (errorCounter == 0){
        jguSubmitter.click();
    } else {
        jguNotification.style.display="block";
        jguNotification.innerText=errorMessage;
        if (jguNotification.classList.contains('successful')){
            jguNotification.classList.remove('successful');
        }
    }
}