function checkTaskData(){

    /*
    Zu Beginn initialisieren wir die DOM-Elemente.
    Beachte, dass taskTime, taskLevel und taskTopic jeweils eine Zahl sind, z.B. bei der Zeit:
    "1" => 10 Minuten, der Wert "1" wird in diesem Fall eingelesen
     */

    let taskName = document.getElementById("jgu-task-name");
    let taskTopic = document.getElementById("jgu-topic");
    let taskTime = document.getElementById("jgu-time");
    let taskLevel = document.getElementById("jgu-level");
    let taskTextCode = document.getElementById("jgu-task-code");
    let taskResult = document.getElementById("jgu-task-result");
    let taskSubmitter = document.getElementById("jgu-submit");
    let jguNotification = document.getElementById("jgu-notification");

    let errorCount = 0;
    let errorMessage = "";

    if (taskName.value.length < 4){
        errorCount++;
        errorMessage = "Der Aufgabentitel ist zu kurz.";
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

    if (errorCount == 0){
        taskSubmitter.click();
    } else {
        jguNotification.style.display="block";
        jguNotification.innerText = errorMessage;
    }

}