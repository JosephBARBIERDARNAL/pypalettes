document.addEventListener('DOMContentLoaded', () => {
    fetch('https://raw.githubusercontent.com/JosephBARBIERDARNAL/pypalettes/main/pypalettes/palettes.csv')
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n').slice(1);
            const palettes = rows.map(row => {
                const columns = row.split(',');
                const name = columns[0];
                const palette = columns.slice(1, -1).join(',').replace(/[\[\] '"]/g, '');
                const colors = palette.split(',');
                return { name, colors };
            });

            // Function to create color elements for the palette of the day
            function createColorElements(colors) {
                const colorsDiv = document.createElement('div');
                colorsDiv.style.display = 'flex'; // Ensure colors are displayed in a row
                colors.forEach(color => {
                    const colorDiv = document.createElement('div');
                    colorDiv.className = 'color';
                    colorDiv.style.backgroundColor = color.trim();
                    colorsDiv.appendChild(colorDiv);
                });
                return colorsDiv;
            }

            // Get the day of the year
            const now = new Date();
            const start = new Date(now.getFullYear(), 0, 0);
            const diff = now - start;
            const oneDay = 1000 * 60 * 60 * 24;
            const dayOfYear = Math.floor(diff / oneDay);

            // Select a palette of the day based on the day of the year
            const paletteOfTheDay = palettes[dayOfYear % palettes.length];

            // Update Palette of the Day section
            const paletteOfTheDayContainer = document.getElementById('palette-of-the-day-container');
            paletteOfTheDayContainer.innerHTML = ''; // Clear existing content

            const title = document.createElement('span');
            title.id = 'palette-of-the-day-title';
            title.textContent = paletteOfTheDay.name;
            paletteOfTheDayContainer.appendChild(title);

            const colorsDiv = createColorElements(paletteOfTheDay.colors);
            paletteOfTheDayContainer.appendChild(colorsDiv);

            // Add code snippet
            const codeSnippet = `from pypalettes import load_cmap\ncmap = load_cmap('${paletteOfTheDay.name}')`;
            const codeContainer = document.getElementById('palette-of-the-day-code');
            codeContainer.textContent = codeSnippet;

            // Update Colormap section
            const colormapContainer = document.getElementById('colormap-container');
            palettes.forEach(({ name, colors }, index) => {
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

                const codeSnippetContainer = document.createElement('div');
                codeSnippetContainer.className = 'code-snippet';
                const codeSnippet = `from pypalettes import load_cmap\ncmap = load_cmap('${name}')`;
                codeSnippetContainer.textContent = codeSnippet;

                // Add copy button to the code snippet
                const copyCodeButton = document.createElement('button');
                copyCodeButton.textContent = 'Code';
                copyCodeButton.addEventListener('click', () => {
                    navigator.clipboard.writeText(codeSnippet);
                    copyCodeButton.textContent = 'Copied!';
                    setTimeout(() => {
                        copyCodeButton.textContent = 'Code';
                    }, 1200);
                });
                codeSnippetContainer.appendChild(copyCodeButton);

                colormapDiv.appendChild(codeSnippetContainer);

                colormapContainer.appendChild(colormapDiv);

                if ((index + 1) % 4 === 0) {
                    const clearfix = document.createElement('div');
                    clearfix.className = 'clearfix';
                    colormapContainer.appendChild(clearfix);
                }
            });
        })
        .catch(error => console.error('Error fetching the CSV file:', error));
});
