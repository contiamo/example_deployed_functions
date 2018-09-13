process.stdin.setEncoding('utf8');

process.stdin.on('readable', () => {
    const chunk = process.stdin.read();
    if (chunk !== null) {
        process.stdout.write(`Hi there, you said: ${chunk}`);
    }
});

process.stdin.on('end', () => {
    process.stdout.write('end');
});