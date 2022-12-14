let probeArea = document.getElementById("jgu-testklausur-section");
let mainImage = document.getElementById("main-image");

/* Diese unteren Variablen müssen abgesichert werden, da diese ansonsten zu einem Skriptfehler führen
Heißt: Falls die jeweiligen Ids beim Role-Check entfernt werden, wird das Skript hier ein Fehler ausspucken, da
es die Ids nicht finden kann. Per If-Clause funktioniert das (leider) nicht. Alternative: In jede Funktion einbauen.
 */

let klausurArea = document.getElementById("jgu-klausur-id");
let actionArt = document.getElementById("jgu-action-create");

function showProbeKlausur(){
    probeArea.style.display="block";
    klausurArea.style.display="none";
    if (mainImage.classList.contains("mobile-hide")){
        mainImage.classList.remove("mobile-hide");
    }
}

function showCreateKlausur(option){
    let header = document.getElementById("jgu-k-label");
    let paragraph = document.getElementById("jgu-p-label");
    if (option == 1){
        header.innerHTML = '<span class="jgu-brand">Klausur</span> erstellen';
        paragraph.innerText = 'Erstellen Sie hier innerhalb von wenigen Klicks eine Klausur, die Sie dann sich ausgeben können.';
    } else if (option == 2){
        header.innerHTML = '<span class="jgu-brand">Übungsblatt</span> erstellen';
        paragraph.innerText = 'Erstellen Sie hier innerhalb von wenigen Klicks ein Übungsblatt, die Sie dann sich ausgeben können.';
    }
    probeArea.style.display="none";
    klausurArea.style.display="block";
    actionArt.value = option;
    if (mainImage.classList.contains("mobile-hide")){}else{
        mainImage.classList.add("mobile-hide");
    }
}

function showTheme(option){
    let hiddenThemenGebiet = document.getElementById("jgu-themen-area");
    if (option == 0){
        hiddenThemenGebiet.style.display="none";
    } else {
        hiddenThemenGebiet.style.display="block";
    }
}

function showThemeSec(option){
    let hiddenThemenGebiet = document.getElementById("jgu-themen-area-sec");
    if (option == 0){
        hiddenThemenGebiet.style.display="none";
    } else {
        hiddenThemenGebiet.style.display="block";
    }
}

function checkFilterData(){
    let jguFachgebiet = document.getElementById("jgu-fachgebiet");
    let jguTopic = document.getElementById("jgu-topic");
    let jguTime = document.getElementById("jgu-time");
    let jguLevel = document.getElementById("jgu-level");
    let jguSubmitter = document.getElementById("jguSub");

    let errorMessage = "";

    if (jguFachgebiet.value == 0 || jguTopic.value == 0){
        errorMessage = "Bitte wähle ein Fachgebiet und ein Themengebiet aus.";
        alert(errorMessage);
    } else {
        jguSubmitter.click();
    }
}

function move(id_1, id_2){

    let opt_obj = document.getElementById(id_1);
    let sel_obj = document.getElementById(id_2);

    for (let i = 0; i < opt_obj.options.length; i++){

        if (opt_obj.options[i].selected == true ){

            let selected_text = opt_obj.options[i].text;
            let selected_value = opt_obj.options[i].value;

            opt_obj.remove(i);
            i--;

            let new_option_index = sel_obj.options.length;
            sel_obj.options[new_option_index] = new Option( selected_text, selected_value );
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

function checkBeforeDocument(){
    let taskList = document.getElementById("jgu-task-id");
    let subArtDoc = document.getElementById("jgu-op-sub");

    if (taskList.value == ""){
        alert("Bitte wählen Sie mindestens eine Aufgabe aus, um ein Dokument erstellen zu können");
    } else {
        subArtDoc.click();
        // Dokument erstellen oder LATEX-Code ausgeben.
    }
}

function checkFilter(){
    let fachFilter = document.getElementById("jgu-fachgebiet-filter");
    let themeFilter = document.getElementById("jgu-topic-filter");
    let actionArtFilter = document.getElementById("jgu-action-create");
    let subArtFilter = document.getElementById("jgu-op-sub");

    if (fachFilter.value == 0 || themeFilter == 0){
        alert("Bitte wählen Sie ein Fachgebiet und ein Themenbereich aus, um den Filter anwenden zu können.");
    } else {
        actionArtFilter.value = 3;
        subArtFilter.click();
        // Filter anwenden
    }
}