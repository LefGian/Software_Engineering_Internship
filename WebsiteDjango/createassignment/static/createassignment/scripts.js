/*
 Die Funktion checkTaskData überprüft alle Eingaben des Nutzers bevor diese verarbeitet und übermittelt werden.
 Sollten Daten nicht vollständig sein oder komplett fehlen, werden entsprechende Warnungen ausgegeben und die
 Übermittelung wird abgebrochen.


 Zu Beginn initialisieren wir die DOM-Elemente aus der HTML-Datei.
 Beachte, dass taskTime, taskLevel und taskTopic jeweils eine Zahl sind, z.B. bei der Zeit:
 "1" => 10 Minuten, der Wert "1" wird in diesem Fall eingelesen
  */

function checkTaskData(){

    let taskName = document.getElementById("jgu-task-name");
    let taskTopic = document.getElementById("jgu-topic");
    let overTopic = document.getElementById("jgu-fachgebiet");
    let taskTime = document.getElementById("jgu-time");
    let taskLevel = document.getElementById("jgu-level");
    let taskTextCode = document.getElementById("jgu-task-code");
    let taskResult = document.getElementById("jgu-task-result");
    let taskSubmitter = document.getElementById("jgu-submit");
    let jguNotification = document.getElementById("jgu-notification");

    // errorCount entspricht der Anzahl von Fehlermeldungen
    // errorMessage entspricht der Nachricht, die dem Nutzer als Rückmeldung dienen soll

    let errorCount = 0;
    let errorMessage = "";

    if (taskName.value.length < 4){
        errorCount++;
        errorMessage = "Der Aufgabentitel ist zu kurz.";
    } else if (overTopic.value === ""){
      errorCount++;
      errorMessage = "Bitte wählen Sie ein Fachgebiet aus.";
    } else if (taskTopic.value === ""){
        errorCount++;
        errorMessage = "Bitte wählen Sie ein Themengebiet aus.";
    } else if (taskTime.value === ""){
        errorCount++;
        errorMessage = "Bitte wählen Sie eine Zeit für Ihre Aufgabe aus.";
    } else if (taskLevel.value === ""){
        errorCount++;
        errorMessage = "Bitte wählen Sie eine Schwierigkeitsstufe aus.";
    } else if (taskTextCode.value.length < 10){
        errorCount++;
        errorMessage = "Ihre Aufgabe ist zu kurz.";
    } else if (taskResult.value.length < 10){
        errorCount++;
        errorMessage = "Ihre Lösung ist zu kurz.";
    }

    // Wenn der errorCount null ist, sprich keine Fehler vorher gefunden worden sind, so kann die Übermittlung erfolgen.

    if (errorCount == 0){
        taskSubmitter.click();
    } else {
        jguNotification.style.display="block";
        jguNotification.innerText = errorMessage;

        // In der folgenden Bedingung wird der "Successfor"-Marker entfernt, sodass Fehlermeldungen in rot
        // dargestellt werden können.

        if (jguNotification.classList.contains('successful')){
            jguNotification.classList.remove('successful');
        }
    }
}

/*
Die Funktion showTheme sorgt dafür, dass bei der Auswahl eines Fachgebiets die Themengebiete nach erfolgreichem
Laden (Django) angezeigt werden. Dabei kann man der Funktion einen Parameter übergeben.

option 0 => Themengebiete ausblenden
option 1 => Themengebiete anzeigen
 */


function showTheme(option){
    let hiddenThemenGebiet = document.getElementById("themengebiet-id");
    if (option==0){
        hiddenThemenGebiet.style.display="none";
    } else {
        hiddenThemenGebiet.style.display="block";
    }
}

/*
Die Funktion chose_fachgebiet_and_submit() setzt in der Form den Wert vhon "chose_fachgebiet" auf 1. Dieser Wert ist
wichtig, sodass in Django unterschieden werden kann zwischen einem normalen Submit und einem Fachgebiet-Submit.
 */

function chose_fachgebiet_and_submit(){
    document.getElementById('chose_fachgebiet').value = 1;
    document.getElementById('myform').submit();
}