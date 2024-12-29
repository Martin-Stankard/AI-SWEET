const fs = require('fs');
const path = require('path');

// Path where the output will be saved (persistent location on host)
const outputPath = path.join(__dirname, '../../stuff/output/testerOutput.txt');

// Write to the file
fs.writeFileSync(outputPath, 'This is the output from tester.js\n');

console.log('Output written to', outputPath);
