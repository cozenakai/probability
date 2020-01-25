// この中にtrue, false, true, false...みたいに結果が入る
let finalResult = [];

// サイコロの合計がルールにマッチしているかどうかtrue falseを返す関数
function saikoro(){
  // 1. サイコロを３回振って合計をだす
  let sum = 0;
  for (let i=0; i <3; i++){
    let result = Math.floor( Math.random() * (6 + 1 - 1) ) + 1 ;
     sum += result;
  }
  // 2. 合計が12以上でかつ、１８未満かどうかを true false で返す
  if (sum > 12 && sum < 18){
    return true
  } else {
    return false
  }
}

// サイコロがルールにマッチしらtrue, falseをresuletという配列に追加する（1000回繰り返す）
for (let i = 0; i < 1000; i++){
  finalResult.push(saikoro())
} 

// true の数を調べる
let trued = 0;
for (var i = 0;  i < finalResult.length; i++) {
    if(finalResult[i] === true){
        trued++;//truedを加算
    }
}


// 確率を計算する
alert(trued/finalResult.length) 