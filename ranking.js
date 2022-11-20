
const fp = document.getElementById("fp");
const submit = document.getElementById("submit");
const result = document.querySelector(".result");
const jsonurl = "ranking.json";    // 読み込むJSONファイル
const pyurl ="";//pythonのurl

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

function formatJSON(json){
    console.log(json);
 
    // JSONファイルを整形して表示
    let html1 = "";
    let html2 = "";
    for(let rank of json.kcal_ranking){
        html1 += "<li>" + rank.name +  "</li>";
        html1 +="<ul><li>" + rank.kcal + "</li></ul>";
    }
    document.getElementById("result1").innerHTML = html1;

    for(let rank of json.step_ranking){
        html2 += "<li>" + rank.name +  "</li>";
        html2 +="<ul><li>" + rank.step + "</li></ul>";
    }
    document.getElementById("result2").innerHTML = html2;
}
 
// 起動時の処理
window.addEventListener("load", ()=>{
 
    fetch(jsonurl)
        .then( response => response.json())
        .then( data => formatJSON(data));
 
});