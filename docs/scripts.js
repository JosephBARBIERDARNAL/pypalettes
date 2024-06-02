document.addEventListener('DOMContentLoaded', () => {
    const paletteOfTheDayName = "Abbott"; // Change this to update the palette of the day
    const paletteOfTheDayColors = ["#9C140D", "#E36752", "#BB8967", "#8A4F3A", "#468144", "#2A5D3B", "#427272", "#2D4C4C"]; // Change this to update the colors

    // Function to create color elements for the palette of the day
    function createColorElements(colors) {
        const colorsDiv = document.createElement('div');
        colorsDiv.style.display = 'flex'; // Ensure colors are displayed in a row
        colors.forEach(color => {
            const colorDiv = document.createElement('div');
            colorDiv.className = 'color';
            colorDiv.style.backgroundColor = color;
            colorsDiv.appendChild(colorDiv);
        });
        return colorsDiv;
    }

    // Update Palette of the Day section
    const paletteOfTheDayContainer = document.getElementById('palette-of-the-day-container');
    paletteOfTheDayContainer.innerHTML = ''; // Clear existing content

    const title = document.createElement('span');
    title.id = 'palette-of-the-day-title';
    title.textContent = paletteOfTheDayName;
    paletteOfTheDayContainer.appendChild(title);

    const colorsDiv = createColorElements(paletteOfTheDayColors);
    paletteOfTheDayContainer.appendChild(colorsDiv);

    // Add code snippet
    const codeSnippet = `from purrpalette import PurrPalette\npurr = PurrPalette()\ncmap = purr.load_cmap('${paletteOfTheDayName}')`;
    const codeContainer = document.getElementById('palette-of-the-day-code');
    codeContainer.textContent = codeSnippet;

    fetch('https://raw.githubusercontent.com/JosephBARBIERDARNAL/purrpalette/main/purrpalette/palettes.csv')
        .then(response => response.text())
        .then(data => {
            const colormapContainer = document.getElementById('colormap-container');
            const rows = data.split('\n').slice(1);
            rows.forEach((row, index) => {
                const columns = row.split(',');
                const name = columns[0];
                const palette = columns.slice(1, -1).join(',').replace(/[\[\] '"]/g, '');
                const colors = palette.split(',');

                if (name && colors.length) {
                    const colormapDiv = document.createElement('div');
                    colormapDiv.className = 'colormap';

                    const titleContainer = document.createElement('div');
                    titleContainer.className = 'title-container';

                    const copyButton = document.createElement('button');
                    copyButton.textContent = `${name}`;
                    copyButton.addEventListener('click', () => {
                        navigator.clipboard.writeText(name);
                        const originalText = copyButton.textContent;
                        copyButton.textContent = 'Copied!';
                        setTimeout(() => {
                            copyButton.textContent = originalText;
                        }, 2000);
                    });
                    titleContainer.appendChild(copyButton);

                    colormapDiv.appendChild(titleContainer);

                    const colorsDiv = document.createElement('div');
                    colorsDiv.className = 'colors';
                    colors.forEach(color => {
                        const colorDiv = document.createElement('div');
                        colorDiv.className = 'color';
                        colorDiv.style.backgroundColor = color.trim();
                        colorsDiv.appendChild(colorDiv);
                    });
                    colormapDiv.appendChild(colorsDiv);

                    const codeSnippet = document.createElement('pre');
                    codeSnippet.className = 'code-snippet';
                    codeSnippet.textContent = `from purrpalette import PurrPalette\npurr = PurrPalette()\ncmap = purr.load_cmap('${name}')`;
                    colormapDiv.appendChild(codeSnippet);

                    colormapContainer.appendChild(colormapDiv);

                    if ((index + 1) % 4 === 0) {
                        const clearfix = document.createElement('div');
                        clearfix.className = 'clearfix';
                        colormapContainer.appendChild(clearfix);
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching the CSV file:', error));
});
