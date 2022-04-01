
//Die Funktion openOverleaf() ruft die angegebene Seite (siehe Variable "ovearLeafLink") in einem neuen Tab auf

function openOverleaf(){
    let overleafLink = "https://latex.zdv.uni-mainz.de/";
    window.open(overleafLink);
}

// Die Funktion copyToClipboard() kopiert den (LaTeX-)Code aus der Textbox in den Clipboard.

function copyToClipboard(){
    let textarea = document.getElementById("latex-textarea");
    textarea.select();
    textarea.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(textarea.value);
    copySuccessfull();
}

// copySuccessfull signalisiert dem Nutzer, dass der Kopiervorgang erfolgreich war (Button wird grün)

function copySuccessfull(){
    let copyBtn = document.getElementById("copy-button");
    if (copyBtn.classList.contains("btn-danger")){
        copyBtn.classList.remove("btn-danger");
        copyBtn.classList.add("btn-success");
        copyBtn.innerText = "Erfolgreich kopiert!";
    }
    setTimeout(function() {
        if (copyBtn.classList.contains("btn-success")){
            copyBtn.classList.remove("btn-success");
            copyBtn.classList.add("btn-danger");
            copyBtn.innerText = "Code kopieren";
        }
    }, 2000);
}

/*
startDownload erstellt eine Datei anhand gegebener Parameter und DOM-Element und lädt diese dann automatisch runter.
So kann der LaTeX-Code aus der Textarea in eine .TEX-Datei übergeben werden und heruntergeladen werden.
 */

function startDownload(filename, text) {
    const element = document.createElement('a');
    const blob = new Blob([text], { type: 'plain/text' });
    const fileUrl = URL.createObjectURL(blob);
    element.setAttribute('href', fileUrl);
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

/*
downloadFile() sammelt die notwendigen Informationen (Parameter) und gibt diese der Funktion startDownload() weiter.
Nach dem Start des Downloads wird dem Nutzer im anschließendem (identisch wie bei der Copy-Funktion) ein Feedback
ausgegeben.
 */

function downloadFile(){
    let latexCode = document.getElementById("latex-textarea").value;
    let fileName = "jg4u-latex.tex";
    startDownload(fileName, latexCode);

    let downloadButton = document.getElementById("download-button");
    if (downloadButton.classList.contains("btn-danger")){
        downloadButton.classList.remove("btn-danger");
        downloadButton.classList.add("btn-success");
        downloadButton.innerText = "Download gestartet!";
    }
    setTimeout(function() {
        if (downloadButton.classList.contains("btn-success")){
            downloadButton.classList.remove("btn-success");
            downloadButton.classList.add("btn-danger");
            downloadButton.innerText = "Code herunterladen";
        }
    }, 2000);
}