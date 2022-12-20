#!/usr/bin/node
const vars = process.argv.slice(2).map(Number).sort((a, b) => a - b);
vars.length > 1 ? console.log(Math.min(...vars)) : console.log(0);
