document.addEventListener('DOMContentLoaded', () => {
    fetch('purrpalette/palettes.csv')
        .then(response => response.text())
        .then(data => {
            const colormapContainer = document.getElementById('colormap-container');
            const rows = data.split('\n').slice(1);
            rows.forEach((row, index) => {
                const columns = row.split(',');
                const name = columns[0];
                const palette = columns.slice(1, -1).join(',').replace(/[\[\] '"]/g, ''); // Handles cases where the palette contains commas
                const colors = palette.split(',');

                if (name && colors.length) {
                    const colormapDiv = document.createElement('div');
                    colormapDiv.className = 'colormap';

                    const title = document.createElement('h2');
                    title.textContent = name;
                    colormapDiv.appendChild(title);

                    const colorsDiv = document.createElement('div');
                    colorsDiv.className = 'colors';
                    colors.forEach(color => {
                        const colorDiv = document.createElement('div');
                        colorDiv.className = 'color';
                        colorDiv.style.backgroundColor = color.trim(); // Ensure color codes are trimmed
                        colorsDiv.appendChild(colorDiv);
                    });
                    colormapDiv.appendChild(colorsDiv);

                    const copyButton = document.createElement('button');
                    copyButton.textContent = 'Copy';
                    copyButton.addEventListener('click', () => {
                        navigator.clipboard.writeText(name);
                        const originalText = copyButton.textContent;
                        copyButton.textContent = 'Copied!';
                        setTimeout(() => {
                            copyButton.textContent = originalText;
                        }, 2000);
                    });
                    colormapDiv.appendChild(copyButton);

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
