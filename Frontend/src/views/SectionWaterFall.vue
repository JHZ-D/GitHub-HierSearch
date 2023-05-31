<template>
  <div id="SectionWhole">
  <n-layout style="background-color: rgba(255, 255, 255, 0);">
    <n-layout-header bordered id="header">
      <n-space id="head-space" size="huge" align="baseline">
        <n-h1>Github层次化学习系统</n-h1>
        <n-tooltip trigger="hover">
          <template #trigger>
            <n-button ghost circle size="small" @click="showModal = true"><n-icon
                size="20"><help-icon /></n-icon></n-button>
          </template>
          帮助
        </n-tooltip>
      </n-space>
    </n-layout-header>
    <n-grid :cols="7" :rows="1" :col-gap="32" :row-gap="16" class="grid">
      <n-grid-item span="5">
          <div class="g6-x" id="containerG6" ref="containerG6"><img id="image" src="../assets/legendnew.gif" width="200" /></div>
      </n-grid-item>
      <n-grid-item span="2">
        <n-grid :cols="1" :rows="2" :row-gap="16" class="mygrid">
          <n-grid-item span="1">
            <!-- <n-card title="Model–view–viewmodel" size="huge" class="mycard"> -->
              <!-- <n-card :title="crepo?'NoneDay/CellReport':'Vue.js'" size="huge" class="mycard"> -->
                <n-card :title="title" size="huge" class="mycard">
                <!-- <n-card title="Vue.js" size="huge" class="mycard">
                Vue.js (commonly referred to as Vue; pronounced "view") is an open-source model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications. It was created by Evan You, and is maintained by him and the rest of the active core team members. -->
                <!-- {{crepo?"CellReport 是一个netcore实现的、以复杂统计报表为核心目标的制作、运行工具。支持数据看板、大屏制作。你可以使用数据库、excel文件、api服务、已有报表等为数据源，通过内置的集合函数组织数据，以类excel界面设计最终呈现结果。":'Vue.js (commonly referred to as Vue; pronounced "view") is an open-source model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications. It was created by Evan You, and is maintained by him and the rest of the active core team members.'}} -->
                {{ description }}
                <!-- CellReport 是一个netcore实现的、以复杂统计报表为核心目标的制作、运行工具。支持数据看板、大屏制作。你可以使用数据库、excel文件、api服务、已有报表等为数据源，通过内置的集合函数组织数据，以类excel界面设计最终呈现结果。 -->
              <!-- Model–view–viewmodel (MVVM) is an architectural pattern in computer software that facilitates the separation of the development of the graphical user interface (GUI; the view)—be it via a markup language or GUI code—from the development of the business logic or back-end logic (the model) such that the view is not dependent upon any specific model platform. -->
              <!-- jQuery is a JavaScript framework designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. It is free, open-source software using the permissive MIT License. As of Aug 2022, jQuery is used by 77% of the 10 million most popular websites. Web analysis indicates that it is the most widely deployed JavaScript library by a large margin, having at least 3 to 4 times more usage than any other JavaScript library. -->
              <br><br><br>
              <!-- {{crepo?"Github Repository":'Wikipedia'}} Link: <a href="https://github.com/NoneDay/CellReport" target="_blank">{{crepo?"https://github.com/NoneDay/CellReport":"https://en.wikipedia.org/wiki/Vue.js"}}</a> -->
              {{ type }} Link: <a :href="url" target="_blank">{{ url }}</a>
              <!-- Wikipedia Link: <a href="https://en.wikipedia.org/wiki/Vue.js" target="_blank">https://en.wikipedia.org/wiki/Vue.js</a> -->
              <!-- Wikipedia Link: <a href="https://en.wikipedia.org/wiki/Model–view–viewmodel" target="_blank">https://en.wikipedia.org/wiki/Model–view–viewmodel</a> -->
              <!-- <br><br> -->
              <!-- Github Topic Link: <a href="https://github.com/topics/vue" target="_blank">https://github.com/topics/vue</a> -->
            </n-card>
          </n-grid-item>
          <n-grid-item span="1">
        </n-grid-item>
        </n-grid>
      </n-grid-item>
    </n-grid>
    <!-- <Legend></Legend> -->
    <!-- <n-layout style="height: 93vh;"> -->
      <!-- <div class="waterfall-container" @scroll="handleScroll"> -->
        <n-modal v-model:show="showModal">
          <n-card style="width: 600px;" title="如何使用" :bordered="false"
            size="huge">
            <p>下图是本系统提供的基于Wikipedia和Github的软件开发领域知识图的一部分。通过之前的搜索或点击，您来到了黄圈所代表的知识点所在位置。</p>
            <p>图中的每个椭圆代表一个Wikipedia软件开发领域的知识，每个圆代表一个Github Topic所代表的知识。本系统将它们联系起来，体现在一张图中。</p>
            <p>您可以在下图中选择与本知识点相关的其他知识点跳转到相应页面进行学习。</p>
            <p>知识图右方的卡片提供了本知识点的简要介绍，并提供了相应的Wikipedia或Github链接，您也可以通过链接跳转到对应网站进行详细学习。</p>
            <p>通过点击Github仓库所对应的节点，您可以得到该仓库所依赖的仓库根据相关知识点层次分类结果的可视化展示，从而体会该知识点的知识结构。</p>
            <!-- <n-gradient-text :size="18">注意事项</n-gradient-text> -->
            <br/><p style="font-size: medium;">注意事项</p>
            <p>如果您对这些概念都掌握得比较好，您可以尝试我们提供的<router-link class="link" to="/search"><n-gradient-text
                  type="info">搜索功能</n-gradient-text></router-link>来寻找与自己感兴趣主题相关的Github仓库。</p>
          </n-card>
        </n-modal>
        <!-- <div class="waterfall-content">
          <div class="piping" ref="piping0">
          </div>
          <div class="piping" ref="piping1">
          </div>
          <div class="piping" ref="piping2">
          </div>
          <div class="piping" ref="piping3">
          </div>
        </div> -->
      <!-- </div> -->
    <!-- </n-layout> -->
  </n-layout>
</div>
</template>

<script>
import { defineComponent, h } from 'vue'
// import SectionCard from './SectionCard'
// import store from '../store'
// import router from '../router'
import { useNotification, NAvatar } from 'naive-ui'
import { Help as HelpIcon } from '@vicons/ionicons5'
import { mapState } from 'vuex'
import axios from 'axios'
import G6 from '@antv/g6'
// import graphdata from '@/assets/graph.json'
// import graphdata from '@/assets/wholegraph.json'
// import graphdata from '@/assets/webdevgraph.json'
import graphdata from '@/assets/vuerepo.json'
import graphdata1 from '@/assets/vuerepo2.json'
import repographdata from '@/assets/repodemotree1.json'
import SDdata from '@/assets/SDdata.json'
// import Legend from '@/components/Legend.vue'

// const loadLimit = 20
// let WFmaxContentHeight = 0
// let loadingMessage = null
let showed = false

export default defineComponent({
  data () {
    return {
      loadEnabled: true,
      currentPage: 0,
      loadOver: false,
      messageBox: undefined,
      showModal: false,
      jsonGraphData: graphdata,
      jsonGraphData1: graphdata1,
      graph: null,
      repographdata: repographdata,
      crepo: false,
      result: {},
      title: '',
      description: '',
      url: '',
      type: ''
    }
  },
  components: {
    HelpIcon
    // Legend
  },
  // async created () {
  //   const message = useMessage()
  //   this.messageBox = message
  //   loadingMessage = message.loading('loading learning entry data', { duration: 5000 })
  //   await this.fetchSections()
  // },
  mounted () {
    // 获取参数并赋值给result
    if (this.$route.query.graph) {
      this.result = { graph: JSON.parse(this.$route.query.graph), description: this.$route.query.description, url: this.$route.query.url, title: this.$route.query.title }
    } else {
      this.result = SDdata
      this.result.title = 'Software development'
    }
    this.description = this.result.description
    this.url = this.result.url
    this.title = this.result.title
    this.type = this.url.startsWith('https://en.wikipedia.org/wiki/') ? 'Wikipedia' : 'GitHub Topic'
    const notification = useNotification()
    if (!showed) {
      showed = true
      notification.create({
        title: '提示',
        description: '关于Github层次化学习系统的说明',
        content: `Github层次化学习系统以Wikipedia软件开发领域的层级知识图谱为基础，根据Wikipedia与Github仓库的连接，将该知识图谱延展到Github Topic所代表的知识，并结合实际的Github仓库帮助软件开发初学者进行系统性的软件开发技能学习。
您可以点击左侧的"?"按钮以查看详细说明
        `,
        avatar: () =>
          h(NAvatar, {
            size: 'small',
            round: true,
            src: 'https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg'
          })
      })
    }
    this.initG6()
    // const rnodes = this.repographdata.nodes
    // const redges = this.repographdata.edges
    // rnodes.forEach(node => {
    //   if (!node.style) {
    //     node.style = {}
    //   }
    //   switch (node.type) {
    //     case 'rect': {
    //       node.size = [130, 40]
    //       node.style.fill = '#008792'
    //       break
    //     }
    //     case 'circle': {
    //       node.size = 80
    //       node.style.fill = '#C6E5FF'
    //       break
    //     }
    //   }
    // })
    // redges.forEach(edge => {
    //   if (!edge.style) {
    //     edge.style = {}
    //   }
    //   if (parseInt(edge.target) > 5) {
    //     edge.style.lineDash = [2, 2]
    //     edge.style.endArrow = false
    //   } else {
    //     edge.style.endArrow = { path: G6.Arrow.vee(5, 20, 15), d: 15 }
    //   }
    // })
    this.graph.on('node:click', (e) => {
    // 先将所有当前有 click 状态的节点的 click 状态置为 false
      const clickNodes = this.graph.findAllByState('node', 'click')
      clickNodes.forEach((cn) => {
        this.graph.setItemState(cn, 'click', false)
      })
      const nodeItem = e.item
      // 设置目标节点的 click 状态 为 true
      this.graph.setItemState(nodeItem, 'click', true)
      // this.graph.layout.nodesep(10)
      // this.graph.layout.ranksep(10)
      let parentid = null
      if (nodeItem._cfg.parent && !(this.type === 'GitHub Repository')) {
        parentid = nodeItem._cfg.parent._cfg.id
      }
      axios.get('/getKnowp', { params: { text: nodeItem._cfg.id, parentid: parentid } })
        .then(res => {
          // res.data是后端传回来的结果，假设是一个数组
          // 使用路由跳转到新页面，并把结果作为参数传递
          this.graph.changeData(res.data.graph)
          this.description = res.data.description
          this.url = res.data.url
          this.type = this.url.startsWith('https://en.wikipedia.org/wiki/') ? 'Wikipedia' : 'GitHub Topic'
          this.type = nodeItem._cfg.id.startsWith('rp') ? 'GitHub Repository' : this.type
          // this.$router.push({ name: 'Section', params: { data: res.data } })
        })
      if (nodeItem._cfg.id.startsWith('rp')) {
        this.graph.updateLayout({ type: 'compactBox', direction: 'BT', getHeight: function getHeight () { return 32 }, getVGap: function getVGap () { return 80 } })
      } else {
        this.graph.updateLayout({ type: 'compactBox', direction: 'TB', getVGap: function getVGap () { return 80 } })
      }
      this.title = nodeItem._cfg.model.label
      // if (nodeItem._cfg.id === 'tp445') {
      //   this.graph.changeData(this.jsonGraphData1)
      //   this.graph.updateLayout({ type: 'compactBox', direction: 'TB', getVGap: function getVGap () { return 80 }, getHGap: function getHGap () { return 90 } })
      //   // this.graph.updateLayout({ type: 'compactBox', direction: 'TB', getHeight: function getHeight () { return 32 }, getWidth: function getWidth () { return 16 }, getVGap: function getVGap () { return 80 }, getHGap: function getHGap () { return 60 } })
      //   // this.graph.render()
      //   return
      // }
      // this.graph.data(this.repographdata)
      // // this.graph.layout.direction = 'BT'
      // this.graph.updateLayout({ type: 'compactBox', direction: 'BT', getHeight: function getHeight () { return 32 }, getWidth: function getWidth () { return 16 }, getVGap: function getVGap () { return 80 }, getHGap: function getHGap () { return 60 } })
      // this.graph.render()
      // this.crepo = true
    })
  },
  methods: {
    initG6 () {
      // const graphData = this.jsonGraphData
      const containerG6 = this.$refs.containerG6
      // const nodes = this.jsonGraphData.nodes
      // // const edges = this.jsonGraphData.edges
      // nodes.forEach(node => {
      //   // node.label = node.id
      //   if (!node.style) {
      //     node.style = {}
      //   }
      //   switch (node.type) {
      //     case 'ellipse': {
      //       node.size = [120, 40]
      //       node.style.fill = '#afb4db'
      //       break
      //     }
      //     case 'rect': {
      //       node.size = [130, 40]
      //       node.style.fill = '#008792'
      //       break
      //     }
      //     case 'circle': {
      //       node.size = 80
      //       node.style.fill = '#C6E5FF'
      //       break
      //     }
      //   }
      //   if (node.id === 'jquery') {
      //     node.style.stroke = '#ffd400'
      //     node.style.lineWidth = 3
      //   }
      // })

      this.graph = new G6.TreeGraph({
        container: containerG6,
        width: 800,
        height: 650,
        fitView: true,
        fitCenter: true,
        modes: {
          default: ['drag-canvas', 'zoom-canvas', 'drag-node']
        },
        // defaultNode: {
        //   // size: [100, 40],
        //   style: {
        //     // fill: '#C6E5FF',
        //     stroke: '#5B8FF9'
        //   },
        //   labelCfg: {
        //     style: {
        //       fill: '#00287E',
        //       fontSize: 12
        //     }
        //   }
        // },
        defaultNode: {
          size: 40,
          anchorPoints: [
            [0.5, 0],
            [0.5, 1]
          ]
        },
        defaultEdge: {
          type: 'cubic-vertical'
        },
        layout: {
          type: 'compactBox',
          direction: 'TB',
          excludeInvisibles: true,
          getId: function getId (d) {
            return d.id
          },
          // getHeight: function getHeight () {
          //   return 32
          // },
          getWidth: function getWidth () {
            return 16
          },
          getVGap: function getVGap () {
            return 80
          },
          getHGap: function getHGap () {
            return 40
          }
        }
        // defaultEdge: {
        //   // type: 'cubic-vertical',
        //   type: 'line',
        //   style: {
        //     stroke: '#A3B1BF',
        //     // endArrow: true
        //     endArrow: {
        //       path: G6.Arrow.vee(5, 20, 15), // 使用内置箭头路径函数，参数为箭头的 宽度、长度、偏移量（默认为 0，与 d 对应）
        //       d: 15
        //     }
        //   }
        // },
        // layout: {
        //   type: 'compactBox',
        //   direction: 'TB'
        //   // type: 'dagre',
        //   // type: 'force2',
        //   // rankdir: 'TB'
        //   // nodesep: 25,
        //   // ranksep: 25
        //   // type: 'radial'
        //   // center: [200, 200], // 可选，默认为图的中心
        //   // linkDistance: 50, // 可选，边长
        //   // nodeStrength: 30, // 可选
        //   // edgeStrength: 0.1, // 可选
        //   // nodeSize: 30, // 可选
        //   // onTick: () => { // 可选
        //   //   console.log('ticking')
        //   // }
        // }
      })
      // const centernode = this.graph.findById('0')
      // const neighbors = centernode.getNeighbors()
      this.graph.node(function (node) {
        // const neighbors = node.getNeighbors()
        // let hide = 1
        // for (let i = 0; i < neighbors.length; i++) {
        //   if (neighbors[i].id === '0') {
        //     hide = 0
        //     break
        //   }
        // }
        // if (hide === 1) {

        // let position = 'center'
        // const centernode = this.graph.findById('0')
        // if (!node.getNeighbors().includes(centernode)) {
        //   this.graph.hideItem(node)
        // }
        // if (!neighbors.includes(node)) {
        //   this.graph.hideItem(node)
        // }
        // if ('')
        // let rotate = 0
        // if (node.children === []) {
        //   // position = 'bottom'
        //   rotate = Math.PI / 2
        // }
        if (!node.style) {
          node.style = {}
        }
        switch (node.group) {
          case 0: {
            node.size = [150, 55]
            node.style.fill = '#afb4db'
            node.type = 'ellipse'
            break
          }
          case 1: {
            node.size = [150, 55]
            node.style.fill = '#afb4db'
            node.type = 'ellipse'
            break
          }
          case 4: {
            node.size = [180, 40]
            node.style.fill = '#008792'
            node.type = 'rect'
            break
          }
          case 2: {
            node.size = 100
            node.style.fill = '#C6E5FF'
            node.type = 'circle'
            break
          }
          case 3: {
            node.size = 100
            node.style.fill = '#C6E5FF'
            node.type = 'circle'
            break
          }
        }
        if (node.cur === 1) {
          node.style.stroke = '#ffd400'
          node.style.lineWidth = 3
        }
        return {
          label: node.label,
          labelCfg: {
            // position,
            // offset: 5,
            style: {
              // textAlign: 'start'
            }
          }
        }
      })
      // this.graph.data(this.jsonGraphData)
      this.graph.data(this.result.graph)
      //   const rnodes = this.repographdata.nodes
      // rnodes.forEach(node => {
      //   if (!node.style) {
      //     node.style = {}
      //   }
      //   switch (node.type) {
      //     case 'rect': {
      //       node.size = [130, 40]
      //       node.style.fill = '#008792'
      //       break
      //     }
      //     case 'circle': {
      //       node.size = 80
      //       node.style.fill = '#C6E5FF'
      //       break
      //     }
      //   }
      // })
      // const neighbors = node.getNeighbors()
      //   let hide = 1
      //   for (let i = 0; i < neighbors.length; i++) {
      //     if (neighbors[i].id === '0') {
      //       hide = 0
      //       break
      //     }
      //   }
      //   if (hide === 1) {
      this.graph.render()
      this.graph.fitView()
      // this.graph.fitCenter()
    }
  },
  computed: {
    loadUrl () {
      return '/getLearnSections/' + this.docName
    },
    ...mapState({
      docName: 'doc_name',
      en: 'en'
    })
  }
})
</script>

<style>
.waterfall-container {
  height: 100%;
  /* overflow: auto; */
  display: flex;
  justify-content: center;
}

.waterfall-content {
  margin: auto;
  width: 1240px;
  display: flex;
  align-items: flex-start;
}

.waterfall-content .piping {
  width: 25%;
  padding: 10px;
  padding-bottom: 0px;
}

.mycard {
  padding: 10px;
  word-break: break-all;
  width: 290px;
  border-radius: 5px;
  box-shadow: 0px 0px 5px #888888;
  margin-bottom: 20px;
  /* margin-right: 20px; */
  margin-left: 0;
  height: 100%;
}

.section-id {
  text-align: center;
}

.g6-x {
  /* width: 800px; */
  position: relative;
  width: 90%;
  /* height: 800px; */
  box-sizing: border-box;
  border: 1px solid #ccc;
  margin-right: 1px;
  background-color: rgba(255, 255, 255, 0.7);
}

.grid {
    margin-top: 50px;
    margin-left: 100px;
    margin-right: 30px;
    width: 90%;
    background-color: rgba(255, 255, 255, 0);
}

.mygrid {
    /* margin-top: 50px; */
    /* margin-left: 100px; */
    margin-right: 30px;
    width: 90%;
    background-color: rgba(255, 255, 255, 0);
}

#gridright {
  display: flex;
  flex-direction: column;
}

#image {
  /* margin-left: 80px; */
  position: absolute;
  top: 0;
  right: 0;
  /* opacity: 0.5; */
  /* transform: translate(0, -100%); */
}

#SectionWhole {
  /* background-image: url('../assets/backgd4.jpg'); */
  background-image: linear-gradient(white, #afb4db);
  background-size: cover;
  background-attachment:fixed;
  width: 100%;
  height: 100%;
  background-color:#cccccc;
}

#header {
  height: 8vh;
  justify-content: center;
  display: flex;
  flex-direction: column;
  align-items: left;
  padding-top: 20px;
  padding-left: 55px;
  padding-bottom: 20px;
  background-color:rgba(242, 234, 218,0.7);
  color: #afdfe4;
}</style>
