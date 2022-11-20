const fp = document.getElementById("fp");
const submit = document.getElementById("submit");
const result = document.querySelector(".result");
const url =
  "https://xxxxxxxxxxxx/sumple.py"; // pythonファイルのURL

submit.addEventListener("click", () => {
  let formData = new FormData(fp); // フォームの値をformDataにセット

  async function postData() {      // async await をお忘れなく
    const res = await fetch(url, { // urlへ
      method: "POST",              // POST送信
      body: formData,
    });
    const r = await res.json(); // レスポンスをjsonで受け取る
    result.textContent = "結果 : " + r;
  }
  postData();
});