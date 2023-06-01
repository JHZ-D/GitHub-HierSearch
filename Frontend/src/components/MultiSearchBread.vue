<template>
    <div style="padding: auto">
    <n-breadcrumb class="breadcrumb">
      <n-breadcrumb-item class="breadcrumbitem" v-for="num in chooseArray.length" :key="num">
        <n-dropdown v-bind:options="chooseArray[num-1]" @select="updateObjArr($event, num)" style="height: 40px;">
          <div class="trigger"  v-text="noNext || num < chooseArray.length?objArr[num - 1]:'选择topic'">
          </div>
        </n-dropdown>
      </n-breadcrumb-item>
    </n-breadcrumb></div>
  </template>

<script>
import { defineComponent } from 'vue'
import array from '@/assets/breadarr.json'

export default defineComponent({
  name: 'MultiSearchBread',
  props: {
    info: {
      type: Array,
      required: false,
      default: () => []
    }
  },
  data () {
    return {
      array: array,
      chooseArray: [],
      // el-select选中的数据
      objArr: [],
      noNext: 0,
      chosenCate: ''
    }
  },
  methods: {
    sendMsg () {
      // 第一个参数是自定义的事件名，它携带第二个参数的内容
      // 第二个参数是传递的数据
      const sendData = {
        chosenCate: this.chosenCate,
        objArr: this.objArr
      }
      this.$emit('receive', sendData)
    },
    chooseChildrenArr (val) {
      // 每次重新点击下拉框都要清除，后续下拉框的值，重新为其赋值
      if (val.childrens.length > 0) { // 如果选中的元素，其有子元素，那么保留下一级的下拉框
        // this.obj = {}
        this.chooseArray[val.level + 1] = val.childrens
        this.chooseArray.splice(val.level + 2)
        this.objArr.splice(val.level + 1)
        this.noNext = 0
      } else { // 如果选中的元素，没有子元素，那么只保留切换的下拉框，清除其以下的所有下拉框
        this.chooseArray.splice(val.level + 1)
        this.objArr.splice(val.level + 1)
        this.noNext = 1
      }
    },
    updateObjArr (key, num) {
      const curArray = this.chooseArray[num - 1]
      const chosenArray = curArray.find(o => o.key === key)
      this.objArr[num - 1] = chosenArray.label
      this.chosenCate = chosenArray.id
      this.chooseChildrenArr(chosenArray)
      this.sendMsg()
    }
  },
  mounted () {
    this.objArr = this.info
    for (let i = 0; i < this.objArr.length; i++) {
      const curArray = this.chooseArray[i]
      const chosenArray = curArray.find(o => o.label === this.objArr[i])
      const val = chosenArray
      if (val.childrens.length > 0) { // 如果选中的元素，其有子元素，那么保留下一级的下拉框
        this.chooseArray[val.level + 1] = val.childrens
        this.noNext = 0
      } else { // 如果选中的元素，没有子元素，那么只保留切换的下拉框，清除其以下的所有下拉框
        this.chooseArray.splice(val.level + 1)
        this.noNext = 1
      }
    }
  },
  created () {
    const arr = []
    this.array.forEach(ele => {
      if (ele.level === 0)arr.push(ele)
    })
    /*
      初始化页面，将数据中一级分类保留放入到要便利的数组中
      其核心思路是
      [[一级下拉框数据],[二级下拉框数据],[三级下拉框]....[n级下拉框]  ]
      */
    this.chooseArray[this.chooseArray.length] = arr
  },
  setup () {
    return {
    }
  }
})
</script>

  <style scoped>
  .trigger {
    padding: 4px;
    margin: -4px;
    /* height: 40px; */
    border-radius: inherit;
    /* background-color: rgba(255, 255, 255, 0.4); */
  }

  .breadcrumb {
    /* margin: 0; */
    display: flex;
    /* height: 40px; */
    padding: auto;
    /* flex-direction: row; */
    /* background-color: rgba(255, 255, 255, 0.4); */
  }

  .breadcrumbitem {
    display: flex;
    /* flex-direction: row; */
    color: crimson;
  }
  </style>
