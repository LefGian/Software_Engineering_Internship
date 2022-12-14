let jguContent = document.getElementById("jgu-m-content");

/*
callJGUModal ruft das Modal-Fenster auf, welches beim Anmelden oder beim Registrieren benötigt wird. Zusätzlich sorgt
diese Funktion für eine entsprechende Unterscheidung zwischen beiden Aktionen, sodass man in Django genau unterscheiden
kann zwischen diesen Aktionen.

Parameter 0 => Anmeldung
Parameter 1 => Registrierung
 */

function callJGUModal(option){
    let repPassword = document.getElementById("j-password-repeat");
    let headLabel = document.getElementById("jgu-m-label");
    let headParagraph = document.getElementById("jgu-m-paragraph");
    let mainButton = document.getElementById("jgu-m-btn");
    let jguSubArt = document.getElementById("jgu-mod-art");
    let jguModal = document.getElementById("jgu-modal");

    document.getElementById("jgu-name-id").value="";
    document.getElementById("jgu-password-id").value="";
    document.getElementById("jgu-password-repeat-id").value="";

    if (jguContent.classList.contains("fadeOut")){jguContent.classList.remove("fadeOut");}

    if (option==0) {
      repPassword.style.display = "none";
      headLabel.innerText = "Anmelden";
      headParagraph.innerText = "Melden Sie sich jetzt in Ihrem JG4UBoard Account an.";
      mainButton.innerText = "Anmelden";
      jguSubArt.value = 0;
    } else if (option==1){
        repPassword.style.display = "block";
        headLabel.innerText = "Registrieren";
        headParagraph.innerText = "Erstellen Sie jetzt kostenlos und schnell Ihren JG4UBoard Account.";
        mainButton.innerText = "Registrieren";
        jguSubArt.value = 1;
    }
    jguModal.style.display="block";
    document.getElementById('jgu-mod-art_shown').value = 1;

    let show_burger_nav = document.getElementById('navbarToggle');
    if (show_burger_nav.classList.contains('show')){
        show_burger_nav.classList.remove('show');
    }
}

// CloseModal schließt das Modal-Fenster (animiert).

function closeModal(){
    let jguModal = document.getElementById("jgu-modal");
    if (!jguContent.classList.contains("fadeOut")){jguContent.classList.add("fadeOut");}
    setTimeout(function(){ jguModal.style.display="none";}, 400);
    document.getElementById('jgu-mod-art_shown').value = 0;
    document.getElementById('jgu-notification').innerText = '';
    document.getElementById('jgu-notification').style.display="none";
}

// checkInputData überprüft alle Eingaben im Client ("Vorprüfung") und gibt dann dem Nutzer entsprechende Rückmeldung

function checkInputData(){
    let username = document.getElementById("jgu-name-id");
    let password = document.getElementById("jgu-password-id");
    let passwordRepeat = document.getElementById("jgu-password-repeat-id");
    let jguSubArt = document.getElementById("jgu-mod-art");
    let submitter = document.getElementById("submitBtn");

    let notifier = document.getElementById("jgu-notification");

    let errorMessage = "";
    let errorCounter = 0;

    if (username.value.length < 4){errorCounter++; errorMessage = "Ihr Benutzername ist zu kurz.";}
    if (password.value.length < 4){errorCounter++; errorMessage = "Ihr Passwort ist zu kurz."; }else{
        if (jguSubArt.value!=0){
            if (password.value !== passwordRepeat.value){errorCounter++; errorMessage = "Ihre Passwörter stimmen nicht überein.";}
        }
    }

    if (errorCounter!==0){
        if (errorCounter==2){
            notifier.innerText = "Bitte überprüfen Sie Ihre Eingaben."
        } else {
            notifier.innerText = errorMessage;
        }
        notifier.style.display="block";
    } else {
        submitter.click();
        notifier.style.display="none";
    }
}

window.onclick = function(event) {
    if (event.target == document.getElementById("jgu-modal")){closeModal();}
}