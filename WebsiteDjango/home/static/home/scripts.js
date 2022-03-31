
let probeArea = document.getElementById("jgu-testklausur-section");
let mainImage = document.getElementById("main-image");

// showProbeKLausur zeigt den Probeklausur-Container mit allen Elementen an.

function showProbeKlausur(){
    let klausurArea = document.getElementById("jgu-klausur-id");

    probeArea.style.display="block";
    klausurArea.style.display="none";
    if (mainImage.classList.contains("mobile-hide")){
        mainImage.classList.remove("mobile-hide");
    }
}

// showCreateKlausur zeigt den Klausur-/Übung-Erstellen-Bereich an
// Parameter 1 = Klausur, Parameter 2 = Übung
// Zusätzlich werden alle Eingaben zurückgesetzt beziehungsweise geprüft

function showCreateKlausur(option){
    let header = document.getElementById("jgu-k-label");
    let paragraph = document.getElementById("jgu-p-label");
    let klausurArea = document.getElementById("jgu-klausur-id");
    let actionArt = document.getElementById("jgu-action-create");

    if (option == 1){
        header.innerHTML = '<span class="jgu-brand">Klausur</span> erstellen';
        paragraph.innerText = 'Erstellen Sie hier innerhalb von wenigen Klicks eine Klausur, die Sie sich dann ausgeben lassen können.';
    } else if (option == 2){
        header.innerHTML = '<span class="jgu-brand">Übungsblatt</span> erstellen';
        paragraph.innerText = 'Erstellen Sie hier innerhalb von wenigen Klicks ein Übungsblatt, die sich Sie dann ausgeben lasen können.';
    }
    probeArea.style.display="none";
    klausurArea.style.display="block";
    actionArt.value = option;

    // Die Klasse "mobile-hide" wird dem Bild in diesem Container drangehangen, sodass die HTML-DOM-Elemente nicht über
    // das Bild kommen.

    if (mainImage.classList.contains("mobile-hide")){}else{
        mainImage.classList.add("mobile-hide");
    }
}

/*
Die Funktion showTheme sorgt dafür, dass bei der Auswahl eines Fachgebiets die Themengebiete nach erfolgreichem
Laden (Django) angezeigt werden. Dabei kann man der Funktion einen Parameter übergeben. (Probeklausur-Bereich)

option 0 => Themengebiete ausblenden
option 1 => Themengebiete anzeigen
 */

function showTheme(option){
    let hiddenThemenGebiet = document.getElementById("jgu-themen-area");
    if (option == 0){
        hiddenThemenGebiet.style.display="none";
    } else {
        hiddenThemenGebiet.style.display="block";
    }
}

/*
Die Funktion showThemeSec sorgt dafür, dass bei der Auswahl eines Fachgebiets die Themengebiete nach erfolgreichem
Laden (Django) angezeigt werden. Dabei kann man der Funktion einen Parameter übergeben. (Klausur/Übungs-Bereich)

option 0 => Themengebiete ausblenden
option 1 => Themengebiete anzeigen
 */

function showThemeSec(option){
    let hiddenThemenGebiet = document.getElementById("jgu-themen-area-sec");
    if (option == 0){
        hiddenThemenGebiet.style.display="none";
    } else {
        hiddenThemenGebiet.style.display="block";
    }
}

/*
Die Funktion checkFilterData überprüft alle Eingaben des Nutzers auf Korrektheit und Vollständigkeit. Sollten Daten
den Vorgaben nicht entsprehcen oder fehlen, wird dem Nutzer hierbei eine entsprehcende Meldung ausgegeben.
 */

function checkFilterData(){
    let jguFachgebiet = document.getElementById("jgu-fachgebiet");
    let jguTopic = document.getElementById("jgu-topic");
    let jguTime = document.getElementById("jgu-time");
    let jguLevel = document.getElementById("jgu-level");
    let jguSubmitter = document.getElementById("jguSub");

    let errorMessage = "";

    if (jguFachgebiet.value == 0 || jguTopic.value == 0){
        errorMessage = "Bitte wählen Sie ein Fachgebiet und ein Themengebiet aus.";
        alert(errorMessage);
    }
    else if(jguTime.value == 0 || jguLevel.value == 0){
        errorMessage = 'Bitte wählen Sie eine Schwierigkeit und Zeit aus.';
        alert(errorMessage);
    } else {
        document.getElementById('document-create-test').value = 1;
        document.getElementById('random-tasks').value = 1; 
        jguSubmitter.click();
    }
}

/*
Die Funktion move verschiebt ein Element von der einen Box in die anderen Box. Hierbei übergibt man der Funktion zwei
Parameter: Ursprungsbox, Neue Box. Entsprechend wird dann in dieser Richtung verschoben (Ursprung -> Neu)

Zusätzlich wird in "hiddenTextField" jede Aufgaben-ID gespeichert, sodass man bei einem Neuladen der Seite alle Aufgaben
noch beibehält und diese Information nicht verliert.
 */

function move(id_1, id_2){

    let opt_obj = document.getElementById(id_1);
    let sel_obj = document.getElementById(id_2);

    for (let i = 0; i < opt_obj.options.length; i++){

        if (opt_obj.options[i].selected == true ){

            let selected_text = opt_obj.options[i].text;
            let selected_value = opt_obj.options[i].value;
            let selected_level = opt_obj.options[i].getAttribute('level');
            let selected_time = opt_obj.options[i].getAttribute('time');

            opt_obj.remove(i);
            i--;

            let new_option_index = sel_obj.options.length;
            sel_obj.options[new_option_index] = new Option(selected_text, selected_value);
            sel_obj.options[new_option_index].setAttribute("level", selected_level);
            sel_obj.options[new_option_index].setAttribute("time", selected_time);
        }
    }

    let hiddenFields = {
        "jgu-task-id": "jguRightBox"
    };

    for(const [target, source] of Object.entries(hiddenFields)) {
        let hiddenTextFld = document.getElementById(target);
        hiddenTextFld.value = "";

        let activeOptions = document.getElementById(source);
        for (let i = 0; i < activeOptions.options.length; i++){
            hiddenTextFld.value += activeOptions.options[i].value;
            hiddenTextFld.value += ",";
        }

        if(hiddenTextFld.value.length > 0) {
            hiddenTextFld.value = hiddenTextFld.value.slice(0, -1);
        }
    }
}

// checkBeforeDocument überprüft alle Nutzereingaben bevor ein Dokument erstellt wird. Sollten Daten fehlen, wird dies
// dem Nutzer entsprechend mitgeteilt.

function checkBeforeDocument(){
    let taskList = document.getElementById("jgu-task-id");
    let subArtDoc = document.getElementById("jgu-op-sub");

    if (taskList.value == "" || taskList.value == "[]"){
        alert("Bitte wählen Sie mindestens eine Aufgabe aus, um ein Dokument erstellen zu können");
    } else {
        document.getElementById('document-create-exam').value = 1;
        subArtDoc.click();
    }
}

// checkFilter überprüft alle Angaben und gibt bei fehlenden Daten dem Nutzer eine Rückmeldung

function checkFilter(){
    let fachFilter = document.getElementById("jgu-fachgebiet-filter");
    let themeFilter = document.getElementById("jgu-topic-filter");
    let actionArtFilter = document.getElementById("jgu-action-create");
    let subArtFilter = document.getElementById("jgu-op-sub");
    let filterArt = document.getElementById('jgu-action-create-filter')

    if (fachFilter.value == 0 || themeFilter.value == 0){
        alert("Bitte wählen Sie ein Fachgebiet und Themengebiet, um den Filter anwenden zu können.");
    } else {
        filterArt.value = 3;
        subArtFilter.click();
    }
}

// switch_action sorgt für eine Unterscheidung zwischen Übung- und Klausurerstellen. Zusätzlich werden die Eingaben
// entfernt.

function switch_action(option){
    let subject = document.getElementById('jgu-fachgebiet-filter');
    subject.value = '';
    document.getElementById('jguLeftBox').innerHTML = '';
    document.getElementById('jguRightBox').innerHTML = '';
    document.getElementById('jgu-task-id').value = '';
    showCreateKlausur(option);
    document.getElementById('jgu-form').submit();
}

// reset_subject entfernt das Fachgebiet und ruft dann Probeklausur auf

function reset_subject(){
    document.getElementById('jgu-fachgebiet').selectedIndex = '';
    showProbeKlausur();
}

// refreshCheck hilft bei der Form-Unterscheidung bezüglich Django.

function refreshCheck(){
    if (document.getElementById('jgu-show-results').checked == true){
        document.getElementById('jgu-show-results').value = 1;
    }
    else if (document.getElementById('jgu-show-results').checked == false){
        document.getElementById('jgu-show-results').value = 0;
    }
}