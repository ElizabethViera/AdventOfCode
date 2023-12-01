import { readFileSync } from "fs";

const s = readFileSync("Day 1/input.txt", "utf-8").split("\n");
let total = 0;
for (let line = 0; line < s.length; line++) {
  let arr: string[] = [];
  for (let i = 0; i < s[line].length; i++) {
    if (+Number(s[line][i])) {
      arr.push(s[line][i]);
    }
  }

  total += 10 * Number(arr[0]) + Number(arr[arr.length - 1]);
}

console.log(total);
