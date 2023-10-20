<script>
import axios from 'axios'
//import {formEmits} from "element-plus";
//mport {reactive} from "vue";
//import {ElMessageBox} from "element-plus";
// Vue.prototype.$axios = axios;
export default {
  name: 'CalculatorRate',
  computed: {},
  props: {
    msg: String
  },
  data() {
    return {
      his_show: '0',
      equation: '0',
      change_deposit_text: '',
      isShow1: true,
      isShow2: false,
      isShow3: true,
      isShow4: false,
      isShowHis: false,
      isFreeDeposit:false,
      isShowchange_text: false,
      isDecimalAdded: false,//小数点
      isLeftbracket: false, //左括号
      isRightbracket: false,//右括号
      isOperatorAdded: false,
      isStarted: false,
      deposit_text:'输入定期存款金额',
      inputvalue1: undefined,//存款金额
      inputvalue2: undefined,//存款时长
      rate_deposit: undefined,//存款利率
      inputvalue5: undefined,//要修改的存款时长
      inputvalue6: undefined,//修改后的存款利率
      outputvalue1: undefined,//存款利息
      inputvalue3: undefined,//贷款金额
      inputvalue4: undefined,//贷款时长
      rate_loan: undefined,
      inputvalue7: undefined,//要修改的贷款时长
      inputvalue8: undefined,//修改的贷款利率
      outputvalue2: undefined,//贷款利息
      ansres: [],//ans
      cal_form: ({
        exp: "",
        ans: ""
      })
    }
  },
  methods: {
    //判断符号
    isOperator(character) {
      return ['+', '-', '×', '÷', '**', '%'].indexOf(character) > -1
    },
    //表达式添加
    append(character) {
      //start
      if (this.equation === '0' && !this.isOperator(character)) {
        if (character === '.') {
          this.equation += '' + character
          this.cal_form.exp += '' + character
          this.isDecimalAdded = true
          this.isOperatorAdded = true
        } else {
          this.equation = '' + character
          this.cal_form.exp = '' + character
        }
        this.isStarted = true
        return
      }
      //add operator
      if (this.isOperator(character) && this.isOperatorAdded === false) {
        this.equation += '' + character
        this.cal_form.exp += '' + character
        this.isDecimalAdded = false
        this.isOperatorAdded = true
      }
      //if not operator
      if (!this.isOperator(character)) {
        if (character === '.' && this.isDecimalAdded) {
          return
        }
        if (character === '.') {
          this.isDecimalAdded = true
          this.isOperatorAdded = true
        } else {
          this.isOperatorAdded = false
        }
        this.equation += '' + character
        this.cal_form.exp += '' + character
      }
    },
    //等号计算
    calculate() {
      if (this.isValid(this.equation)) {
        let result = this.equation.replace(new RegExp('×', 'g'), '*')
            .replace(new RegExp('÷', 'g'), '/')
            .replace(new RegExp('Π', 'g'), 'Math.PI')
            .replace(new RegExp('e', 'g'), 'Math.E')
        this.equation = parseFloat(eval(result).toFixed(10)).toString()
        this.cal_form.ans = this.equation
        console.log(this.cal_form)
        this.submitForm()
        this.isDecimalAdded = false
        this.isOperatorAdded = false
      } else {
        this.equation = 'Error'
      }
    },
    //正负翻转
    calculateToggle() {
      if (!this.isStarted) {
        return
      }
      this.equation = this.equation + '* -1'
      this.calculate()
    },
    //计算根号
    calSquare() {
      this.cal_form.exp = '√(' + this.equation + ')'
      this.equation = this.equation.replace(new RegExp('×', 'g'), '*')
          .replace(new RegExp('÷', 'g'), '/')
          .replace(new RegExp('Π', 'g'), 'Math.PI')
          .replace(new RegExp('e', 'g'), 'Math.E')
      this.equation = parseFloat(eval('Math.sqrt(' + this.equation + ')').toFixed(10)).toString()
      this.cal_form.ans = this.equation
      this.submitForm()
    },
    lnclick(){
      this.cal_form.exp = 'ln(' + this.equation + ')'
      this.equation = this.equation.replace(new RegExp('×', 'g'), '*')
          .replace(new RegExp('÷', 'g'), '/')
          .replace(new RegExp('Π', 'g'), 'Math.PI')
          .replace(new RegExp('e', 'g'), 'Math.E')
      this.equation = parseFloat(eval('Math.log(' + this.equation + ')').toFixed(10)).toString()
      this.cal_form.ans = this.equation
      this.submitForm()
    },
    logclick(){
      this.cal_form.exp = 'log(' + this.equation + ')'
      this.equation = this.equation.replace(new RegExp('×', 'g'), '*')
          .replace(new RegExp('÷', 'g'), '/')
          .replace(new RegExp('Π', 'g'), 'Math.PI')
          .replace(new RegExp('e', 'g'), 'Math.E')
      this.equation = parseFloat(eval('Math.log(' + this.equation + ')').toFixed(10)).toString()
      this.equation = parseFloat(eval(this.equation +'/'+'Math.log(10)').toFixed(10)).toString()
      this.cal_form.ans = this.equation
      this.submitForm()
    },
    expclick(){
      this.cal_form.exp = 'e^' + this.equation
      this.equation = this.equation.replace(new RegExp('×', 'g'), '*')
          .replace(new RegExp('÷', 'g'), '/')
          .replace(new RegExp('Π', 'g'), 'Math.PI')
          .replace(new RegExp('e', 'g'), 'Math.E')
      this.equation = parseFloat(eval('Math.exp(' + this.equation + ')').toFixed(10)).toString()
      this.cal_form.ans = this.equation
      this.submitForm()
    },
    //计算三角函数
    calTri(op) {
      this.cal_form.exp = op + '(' + this.equation + ')'
      this.equation = this.equation.replace(new RegExp('×', 'g'), '*')
          .replace(new RegExp('÷', 'g'), '/')
          .replace(new RegExp('Π', 'g'), 'Math.PI')
          .replace(new RegExp('e', 'g'), 'Math.E')
      this.equation = parseFloat(eval('Math.' + op + '(' + this.equation + ')').toFixed(10)).toString()
      this.cal_form.ans = this.equation
      this.submitForm()
    },
    //清零
    clear() {
      this.isShowHis = false
      this.equation = '0'
      this.show = '0'
      this.idDecimalAdded = false
      this.isOperatorAdded = false
      this.isLeftbracket = false
      this.isRightbracket = false
      this.isStarted = false
    },
    //回退
    Deletedlast() {
      if (this.equation.length === 1) {
        this.equation = '0'
        this.cal_form.exp = '0'
      } else
        this.equation = this.equation.substring(0, this.equation.length - 1)
      this.cal_form.exp = this.cal_form.exp.substring(0, this.show.length - 1)
    },
    //括号匹配问题
    isValid(str) {
      let strArr = str.split(''),
          left = [];// 空栈
      for (let i = 0; i < strArr.length; i++) {
        if (strArr[i] === '(' || strArr[i] == '[' || strArr[i] == '{') {
          left.push(strArr[i]) //左括号入栈
        } else {
          if (strArr[i] == ')' && left.pop() != '(') {
            return false //结束循环
          }
          if (strArr[i] == ']' && left.pop() != '[') {
            return false
          }
          if (strArr[i] == '}' && left.pop() != '{') {
            return false
          }
        }
      }
      return left.length == 0
    },
    //计算器切换
    changeshow1() {
      this.isShowchange_text=false
      this.isShow1 = !this.isShow1
      this.isShow2 = !this.isShow2
    },
    changeshow2() {
      this.isShowchange_text=false
      this.isShow3 = !this.isShow3
      this.isShow4 = !this.isShow4
    },
    change_deposit_type(){
      if(!this.isFreeDeposit){
        this.isFreeDeposit=true
        this.deposit_text='输入活期存款金额'
      }
      else {
        this.isFreeDeposit=false
        this.deposit_text='输入定期存款金额'
      }
    },
    //查看历史记录
    ansclicked() {
      this.isShowHis = !this.isShowHis
      axios.get("http://localhost:5000/cals",).then(res => {
        let result = res.data.results
        this.ansres = result
        this.ansres.forEach((ele) => {
          this.equation = ele["ans"]
        })
        console.log(result, this.ansres)
      })


    },
    //添加运算
    submitForm() {
      axios.post('http://localhost:5000/cals/', this.cal_form).then((res) => {
        console.log(res)
      })
    },
    //计算存款利息
    cal_deposit() {
      let i;
      const array = [0.25, 0.5, 1, 2, 3, 5]
      if(this.isFreeDeposit) {
        axios.get(`http://localhost:5000/deposits/7`,).then(res => {
          this.rate_deposit = res.data.result.deposit_rate
          this.outputvalue1 = this.rate_deposit * this.inputvalue1 * this.inputvalue2 * 0.01
        })
      }else
        {
          for (i = 0; i < array.length; i++) {
            if (this.inputvalue2 == array[i]) {
              axios.get(`http://localhost:5000/deposits/${i + 1}`,).then(res => {
                this.rate_deposit = res.data.result.deposit_rate
                this.outputvalue1 = this.rate_deposit * this.inputvalue1 * this.inputvalue2 * 0.01
              })
            }
          }
        }
      },
    //计算贷款利息
    cal_loan() {
      let i;
      if (this.inputvalue4 == '0.5')
        i = 1;
      else if (this.inputvalue4 == '1')
        i = 2
      else if (this.inputvalue4 > '1' && this.inputvalue4 < '3')
        i = 3
      else if (this.inputvalue4 >= '3' && this.inputvalue4 < '5')
        i = 4
      else if (this.inputvalue4 == '5')
        i = 5
      axios.get(`http://localhost:5000/loans/${i}`,).then(res => {
        this.rate_loan = res.data.result.loan_rate
        this.outputvalue2 = this.rate_loan * this.inputvalue3 * this.inputvalue4 * 0.01
      })
    },
    //修改存款利率
    change_deposit_rate() {
      let i;
      let flag1 = 0;
      let array1 = [0.25, 0.5, 1, 2, 3, 5];
      for (i = 0; i < array1.length; i++) {
        if (this.inputvalue5 == array1[i]) {
          flag1 = 1;
          axios.put(`http://localhost:5000/deposits/${i + 1}`, ({
            deposit_time: this.inputvalue5,
            deposit_rate: this.inputvalue6
          })).then(res => {
            console.log(res)
          })
        }
      }
      if (flag1 == 1) {
        this.isShowchange_text = true
        this.change_deposit_text = '修改成功'
      } else {
        this.isShowchange_text = true
        this.change_deposit_text = '没有该时长的利率'
      }
    },
    //修改贷款利率
    change_loan_rate() {
      let i;
      let flag2=0;
      if (this.inputvalue7 == '0.5') {
        i = 1
        flag2=1
      }
      else if (this.inputvalue7 == '1') {
        i = 2
        flag2=1
      }
      else if (this.inputvalue7 == '1-3') {
        i = 3
        flag2=1
      }
      else if (this.inputvalue7 == '3-5') {
        i = 4
        flag2=1
      }
      else if (this.inputvalue7 == '5') {
        i = 5
        flag2=1
      }
      if (flag2 == 1) {
        axios.put(`http://localhost:5000/loans/${i}`, ({
          loan_time: this.inputvalue7,
          loan_rate: this.inputvalue8
        })).then(res => {
          console.log(res)
        })
        this.isShowchange_text = true
        this.change_deposit_text = '修改成功'
      } else {
        this.isShowchange_text = true
        this.change_deposit_text = '没有该时长的利率'
      }
    },
  }
}

</script >

<template>
  <button class = 'btn1' v-show="isShow1" @click="changeshow1">科学计算器</button>
  <div class ="calculator" v-show="isShow1">
    <div class="result"  style="grid-area: result" >
      {{equation}}
    </div>
    <div class="history_show" v-show="isShowHis">
      <div v-for=" item in ansres" :key="item" >
        {{item.exp+'='+item.ans}}
      </div>
    </div>
    <button style="grid-area: ac" @click="clear">AC</button>
    <button style="grid-area: plus-minus" @click="calculateToggle">±</button>
    <button style="grid-area: percent" @click="append('%')">%</button>
    <button style="grid-area: add" @click="append('+')">+</button>
    <button style="grid-area: subtract" @click="append('-')">-</button>
    <button style="grid-area: multiply" @click="append('×')">×</button>
    <button style="grid-area: divide" @click="append('÷')">÷</button>
    <button style="grid-area: equal" @click="calculate">=</button>
    <button style="grid-area: backclick" @click="Deletedlast">X</button>
    <button style="grid-area: leftbracket" @click="append('(')">(</button>
    <button style="grid-area: rightbracket" @click="append(')')">)</button>
    <button style="grid-area: numpower" @click="append('**')">x^</button>
    <button style="grid-area: squareclick" @click="calSquare">√x</button>
    <button style="grid-area: ansclick" @click="ansclicked">ANS</button>
    <button style="grid-area: sinclick" @click="calTri('sin')">sin</button>
    <button style="grid-area: cosclick" @click="calTri('cos')">cos</button>
    <button style="grid-area: tanclick" @click="calTri('tan')">tan</button>
    <button style="grid-area: paiclick" @click="append('Π')">Π</button>
    <button style="grid-area: eclick" @click="append('e')">e</button>
    <button style="grid-area: lnclick" @click="lnclick">ln</button>
    <button style="grid-area: logclick" @click="logclick">log</button>
    <button style="grid-area: expclick" @click="expclick">exp</button>

    <button style="grid-area: number-1" @click="append(1)">1</button>
    <button style="grid-area: number-2" @click="append(2)">2</button>
    <button style="grid-area: number-3" @click="append(3)">3</button>
    <button style="grid-area: number-4" @click="append(4)">4</button>
    <button style="grid-area: number-5" @click="append(5)">5</button>
    <button style="grid-area: number-6" @click="append(6)">6</button>
    <button style="grid-area: number-7" @click="append(7)">7</button>
    <button style="grid-area: number-8" @click="append(8)">8</button>
    <button style="grid-area: number-9" @click="append(9)">9</button>
    <button style="grid-area: number-0" @click="append(0)">0</button>

    <button style="grid-area: dot" @click="append('.')">.</button>
  </div>

  <button class ='btn2' v-show="isShow2" @click="changeshow1">利率计算器</button>
  <div v-show="isShow2">
    <button class='deposit' v-show="isShow3" @click="changeshow2">存款</button>
    <div  class ='rate_calculator1' style="grid-area: rate_result1" v-show="isShow3">
      <h1 class = 'text' style="grid-area: text1" @click="change_deposit_type">{{deposit_text}}</h1>
      <h1 class = 'text' style="grid-area: text2">存款时长（单位：年）:</h1>
      <input class = 'text_box' style="grid-area: text_box1" type="text" placeholder="输入存款金额" v-model="inputvalue1">
      <input class = 'text_box' style="grid-area: text_box2" type="text" placeholder="存款时长（单位：年)" v-model="inputvalue2">
      <h1 class = 'rate_btn1' style="grid-area: btn1" @click="cal_deposit">计算存款利息:</h1>
      <input class = 'text_box' style="grid-area: text_box3" type="text" placeholder="存款利息" v-model="outputvalue1">
      <h1 class = 'text' style="grid-area: text5">修改的存款利率时长（单位：年）:</h1>
      <h1 class = 'text' style="grid-area: text6">修改后的存款利率 :</h1>
      <input class = 'text_box' style="grid-area: text_box7" type="text" placeholder="修改的存款利率时长（单位：年）" v-model="inputvalue5">
      <input class = 'text_box' style="grid-area: text_box8" type="text" placeholder="修改后的存款利率" v-model="inputvalue6">
      <h1 class='change_text' style="grid-area: change_text" v-show="isShowchange_text">{{change_deposit_text}}</h1>
      <h1 class="rate_btn3" style="grid-area: text11" @click="change_deposit_rate">确定修改:</h1>
    </div>
  </div>
  <div v-show="isShow2">
    <button class='deposit'  v-show="isShow4" @click="changeshow2">贷款</button>
    <div class ='rate_calculator2' style="grid-area: rate_result2" v-show="isShow4">
      <h1 class = 'text' style="grid-area: text3">输入贷款金额:</h1>
      <h1 class = 'text' style="grid-area: text4">贷款时长（单位：年）:</h1>
      <input class = 'text_box' style="grid-area: text_box4" type="text" placeholder="输入贷款金额" v-model="inputvalue3">
      <input class = 'text_box' style="grid-area: text_box5" type="text" placeholder="贷款时长（单位：年)" v-model="inputvalue4">
      <h1 class = 'rate_btn2' style="grid-area: btn2" @click="cal_loan">计算贷款利息:</h1>
      <input class = 'text_box' style="grid-area: text_box6" type="text" placeholder="贷款利息" v-model="outputvalue2">
      <h1 class = 'text' style="grid-area: text7">修改的贷款利率时长（单位：年）:</h1>
      <h1 class = 'text' style="grid-area: text8">修改后的贷款利率 :</h1>
      <input class = 'text_box' style="grid-area: text_box9" type="text" placeholder="修改的贷款利率时长（单位：年）" v-model="inputvalue7">
      <input class = 'text_box' style="grid-area: text_box10" type="text" placeholder="修改后的贷款利率" v-model="inputvalue8">
      <h1 class='change_text' style="grid-area: change_text" v-show="isShowchange_text">{{change_deposit_text}}</h1>
      <h1 class="rate_btn3" style="grid-area: text12" @click="change_loan_rate">确定修改:</h1>
    </div>
  </div>

</template>

<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #eee;
  .history_show::-webkit-scrollbar {display:none}
}
.calculator{
  --button-width:80px;
  --button-height:80px;
  border:2px solid rgba(255,185,0,0.5);
  display: grid;

  grid-template-areas:
    "history_show history_show history_show history_show history_show history_show history_show"
    "result result result result result result result"
    "ac plus-minus divide  leftbracket rightbracket backclick backclick"
    "number-7 number-8 number-9 multiply eclick  sinclick lnclick"
    "number-4 number-5 number-6 subtract paiclick cosclick expclick"
    "number-1 number-2 number-3 add squareclick  tanclick logclick"
    "number-0 dot equal percent numpower  ansclick ansclick";
  grid-template-columns: repeat(7,var(--button-width));
  grid-template-rows: repeat(7,var(--button-height));
  box-shadow: -8px -8px 16px -10px rgba(255,255,255,1),8px 8px 16px -10px rgba(0,0,0,.15);
  padding: 24px;
  border-radius: 20px;
}
.calculator button{
  margin: 8px;
  padding: 0;
  border: 0;
  display: block;
  outline: none;
  border-radius:calc(var(--button-height)/2);
  font-size: 24px;
  font-family: Helvetica;
  font-weight: normal;
  color: #999;
  background: linear-gradient(135deg,rgba(230,230,230,1) 0%,
  rgba(246,246,246,1) 100%);
  box-shadow: -4px -4px 10px -8px rgba(255,255,255,1),
  4px 4px 10px -8px rgba(0,0,0,.3);

}
.calculator button:active{
  box-shadow: -4px -4px 10px -8px rgba(255,255,255,1) inset,
  4px 4px 10px -8px rgba(0,0,0,.3) inset;
}
.result{
  width:520px;
  text-align: right;
  border-bottom: 2px solid rgb(222,184,135) ;
  line-height: var(--button-height);
  font-size: 48px;
  font-family: Helvetica;
//padding: 0 300px;
  padding-left: 20px;
  color:#666;
}
.history_show1{
  display: flex;
  flex-direction: column;
  width:450px;
  overflow-y: auto; //出现垂直滚动条
  div {
    border: 1px solid rosybrown;
  }
}


.history_show{
  color: rgba(128,138,135,0.5);
  width:520px;
  text-align: right;
  line-height: var(--button-height);
  font-size: 48px;
  font-family: Helvetica;
//padding: 0 300px;
  padding-left: 20px;
  overflow: auto;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */

  div {
    border: 1px solid rosybrown;
  }
  color:#666;
}
.btn1{
  display: block;
  margin: 0 auto;
  font-size: 25px;
  padding-bottom: 15px;
  border:none;
}
.btn1:hover {
  color: grey;
  background-color: #eeeeee;
  cursor: pointer;
}
.btn2{
  display: block;
  margin: 0 auto;
  font-size: 25px;
  padding-bottom: 15px;
  border:none;
}
.btn2:hover {
  color: grey;
  background-color: #eeeeee;
  cursor: pointer;
}
.rate_calculator1{
  --h1-width:220px;
  --h1-height:80px;
  width: 1000px;
  border:2px solid rgba(255,185,0,0.5);
  display: grid;

  grid-template-areas:
      "text1 text_box1 text5 text_box7"
      "text2 text_box2 text6 text_box8"
      "btn1 text_box3 text11 change_text";

  grid-template-columns: repeat(4,var(--h1-width));
  grid-template-rows: repeat(3,var(--h1-height));
  box-shadow: -8px -8px 16px -10px rgba(255,255,255,1),8px 8px 16px -10px rgba(0,0,0,.15);
  padding: 24px;
  border-radius: 20px;
}
.rate_calculator2{
  --h1-width:220px;
  --h1-height:80px;
  width: 1000px;
  border:2px solid rgba(255,185,0,0.5);
  display: grid;

  grid-template-areas:
      "text3 text_box4 text7 text_box9"
      "text4 text_box5 text8 text_box10"
      "btn2 text_box6 text12 change_text";

  grid-template-columns: repeat(4,var(--h1-width));
  grid-template-rows: repeat(3,var(--h1-height));
  box-shadow: -8px -8px 16px -10px rgba(255,255,255,1),8px 8px 16px -10px rgba(0,0,0,.15);
  padding: 24px;
  border-radius: 20px;
}
.text{
  width: 220px;
  text-align: center;
  font-size: 15px;
}
.text_box{
  width: 200px;
  height: 30px;
}
.rate_btn1{
  text-align: center;
  width: 200px;
  height: 80px;
  font-size: 15px;
  border: none;
  font-weight: bold;
}
.rate_btn1:hover{
  color: grey;
  background-color: #eeeeee;
  cursor: pointer;
}
.rate_btn2{
  text-align: center;
  width: 200px;
  height: 80px;
  font-size: 15px;
  border: none;
  font-weight: bold;
}
.rate_btn2:hover{
  color: grey;
  background-color: #eeeeee;
  cursor: pointer;
}
.change_text{
  text-align: center;
  width: 220px;
  height: 80px;
  font-size: 20px;
  border: none;
  font-weight: bold;
  color: grey;
}
.rate_btn3{
  text-align: center;
  width: 220px;
  height: 80px;
  font-size: 20px;
  border: none;
  font-weight: bold;
}
.rate_btn3:hover{
  color: grey;
  background-color: #eeeeee;
  cursor: pointer;
}
.deposit{
  padding: 5px;
  border-radius: 20px;
  width: 100px;
  margin: 0 auto;
  border: 0;
  display: block;
  outline: none;
  font-size: 20px;
  font-family: Helvetica;
  font-weight: normal;
  color: black;
  background: linear-gradient(135deg,rgba(230,230,230,1) 0%,
  rgba(246,246,246,1) 100%);
  box-shadow: -4px -4px 10px -8px rgba(255,255,255,1),
  4px 4px 10px -8px rgba(0,0,0,.3);
}
.deposit:hover{
  color: grey;
  background-color: #eeeeee;
  cursor: pointer;
}
</style>
