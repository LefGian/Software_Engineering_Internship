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
        paragraph.innerText = 'Erstellen Sie hier innerhalb von wenigen Klicks eine Klausur, die Sie sich dann ausgeben lassen können.';
    } else if (option == 2){

        header.innerHTML = '<span class="jgu-brand">Übungsblatt</span> erstellen';
        paragraph.innerText = 'Erstellen Sie hier innerhalb von wenigen Klicks ein Übungsblatt, die sich Sie dann ausgeben lasen können.';
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
        errorMessage = "Bitte wählen Sie ein Fachgebiet und ein Themengebiet aus.";
        alert(errorMessage);
    }
    else if(jguTime.value == 0 || jguLevel.value == 0){
        errorMessage = 'Bitte wählen Sie eine Schwierigkeit und Zeit aus.';
        alert(errorMessage);
    } else {
        document.getElementById('document-create-test').value = 1;
        document.getElementById('create-test-exam').value = 1; 
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

function checkBeforeDocument(){
    let taskList = document.getElementById("jgu-task-id");
    let subArtDoc = document.getElementById("jgu-op-sub");

    if (taskList.value == "" || taskList.value == "[]"){
        alert("Bitte wählen Sie mindestens eine Aufgabe aus, um ein Dokument erstellen zu können");
    } else {
        document.getElementById('document-create-exam').value = 1;
        subArtDoc.click();
        // Dokument erstellen oder LATEX-Code ausgeben.
    }
}

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
        
        // Filter anwenden
    }
}


function switch_action(option){
    let subject = document.getElementById('jgu-fachgebiet-filter');
    subject.value = '';
    document.getElementById('jguLeftBox').innerHTML = '';
    document.getElementById('jguRightBox').innerHTML = '';
    document.getElementById('jgu-task-id').value = '';
    showCreateKlausur(option);
    document.getElementById('jgu-form').submit();
}


function reset_subject(){
    document.getElementById('jgu-fachgebiet').selectedIndex = '';
    showProbeKlausur();
}

function refreshCheck(){
    if (document.getElementById('jgu-show-results').checked == true){
        document.getElementById('jgu-show-results').value = 1;
    }
    else if (document.getElementById('jgu-show-results').checked == false){
        document.getElementById('jgu-show-results').value = 0;
    } 
}