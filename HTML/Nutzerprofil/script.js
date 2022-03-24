function checkFirstData(){

    // Zu Beginn erstmal alle DOM-Elemente einlesen

    let jguVorname = document.getElementById("jgu-vorname");
    let jguNachname = document.getElementById("jgu-nachname");
    let jguTopc = document.getElementById("jgu-topic");
    let jguPassword = document.getElementById("jgu-password");
    let jguPasswordNew = document.getElementById("jgu-password-new");
    let jguSubmitter = document.getElementById("jgu-submit");
    let jguNotification = document.getElementById("jgu-notification");

    let errorCounter = 0;
    let errorMessage = "";

    // Nutzereingaben prüfen nach Vorlegen und entsprechend Fehler sammeln, falls was nicht stimmt.

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

    // Falls Fehler vorhanden (errorCode != 0), führen wir den Submit nicht aus. Stattdessen geben wir den Fehler
    // dem Nutzer aus.

    if (errorCounter == 0){
        jguSubmitter.click();
    } else {
        jguNotification.style.display="block";
        jguNotification.innerText=errorMessage;
    }

}