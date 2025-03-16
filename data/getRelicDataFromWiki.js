function parseTableRow(cells) {
    if (cells.length < 4) {
        console.error("Die Zeile hat nicht genügend Zellen.");
        return null;
    }

    // Helper-Funktion, um alles nach ".png" zu entfernen
    function cleanUrl(url) {
        return url ? url.split(".png")[0] + ".png" : "";
    }

    // Erste Zelle: Bildlink aus `src`-Attribut des ersten <img>
    const iconImg = cells[0].querySelector("img");
    const iconUrl = cleanUrl(iconImg ? iconImg.src : "");

    // Zweite Zelle: InnerText
    const name = cells[1].innerText.trim();

    // Dritte Zelle: Bilder aus `span.item-image > span.hidden > img`
    const itemImages = cells[2].querySelectorAll("span.item-image span.hidden img");
    const [head, hand, body, feet] = Array.from(itemImages).map(img => cleanUrl(img.src || ""));

    // Vierte Zelle: InnerText
    const bonuses = cells[3].innerText.trim();

    // Ergebnisobjekt
    return {
        name,
        bonuses,
        iconurl: iconUrl,
        head: head || "",
        hand: hand || "",
        body: body || "",
        feet: feet || ""
    };
}
var tables = document.getElementsByTagName("table")
for (let table of tables) {
    let infodump = [];
    for (let i = 1; i < table.rows.length; i++) {
        infodump.push(parseTableRow(table.rows[i].cells))
    }
    console.log(infodump);
}