#!/usr/bin/node
const vars = process.argv.slice(2);
vars.length > 1 ? console.log(Math.min(...vars)) : console.log(0);
