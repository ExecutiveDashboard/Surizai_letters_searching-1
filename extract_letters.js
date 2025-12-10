const fs = require("fs");
const { readDocx } = require("docx-to-text");

readDocx("PHA letters for Peshawar Allottees.docx")
    .then(text => {

        // Split letters using a unique pattern
        // Example: Each letter starts with "Subject" or "To,"
        const rawLetters = text.split("PHA FOUNDATION");

        let letters = [];
        rawLetters.forEach((part, index) => {
            const cleaned = part.trim();
            if (!cleaned) return;

            // Extract Name & CNIC using regex
            const nameMatch = cleaned.match(/Name[:\- ]+([A-Za-z ]+)/i);
            const cnicMatch = cleaned.match(/CNIC[:\- ]+([0-9\-]+)/i);

            letters.push({
                id: index,
                name: nameMatch ? nameMatch[1].trim() : "Unknown",
                cnic: cnicMatch ? cnicMatch[1].trim() : "Unknown",
                text: cleaned
            });

        });

        fs.writeFileSync(
            "letters_from_docx.json",
            JSON.stringify({ letters }, null, 2)
        );


    })
    .catch(err => console.error(err));
