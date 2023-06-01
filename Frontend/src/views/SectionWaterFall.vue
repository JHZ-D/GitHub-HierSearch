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
                <n-card :title="title" size="huge" class="mycard">
                {{ description }}
              <br><br><br>
              {{ type }} Link: <a :href="url" target="_blank">{{ url }}</a>
            </n-card>
          </n-grid-item>
          <n-grid-item span="1">
        </n-grid-item>
        </n-grid>
      </n-grid-item>
    </n-grid>
        <n-modal v-model:show="showModal">
          <n-card style="width: 600px;" title="如何使用" :bordered="false"
            size="huge">
            <p>下图是本系统提供的基于Wikipedia和Github的软件开发领域知识图的一部分。通过之前的搜索或点击，您来到了黄圈所代表的知识点所在位置。</p>
            <p>图中的每个椭圆代表一个Wikipedia软件开发领域的知识，每个圆代表一个Github Topic所代表的知识。本系统将它们联系起来，体现在一张图中。</p>
            <p>您可以在下图中选择与本知识点相关的其他知识点跳转到相应页面进行学习。</p>
            <p>知识图右方的卡片提供了本知识点的简要介绍，并提供了相应的Wikipedia或Github链接，您也可以通过链接跳转到对应网站进行详细学习。</p>
            <p>通过点击Github仓库所对应的节点，您可以得到该仓库所依赖的仓库根据相关知识点层次分类结果的可视化展示，从而体会该知识点的知识结构。</p>
            <br/><p style="font-size: medium;">注意事项</p>
            <p>如果您对这些概念都掌握得比较好，您可以尝试我们提供的<router-link class="link" to="/search"><n-gradient-text
                  type="info">搜索功能</n-gradient-text></router-link>来寻找与自己感兴趣主题相关的Github仓库。</p>
          </n-card>
        </n-modal>
  </n-layout>
</div>
</template>

<script>
import { defineComponent, h } from 'vue'
import { useNotification, NAvatar } from 'naive-ui'
import { Help as HelpIcon } from '@vicons/ionicons5'
import { mapState } from 'vuex'
import axios from 'axios'
import G6 from '@antv/g6'
import SDdata from '@/assets/SDdata.json'

let showed = false

export default defineComponent({
  data () {
    return {
      loadEnabled: true,
      currentPage: 0,
      loadOver: false,
      messageBox: undefined,
      showModal: false,
      graph: null,
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
  },
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
    this.graph.on('node:click', (e) => {
    // 先将所有当前有 click 状态的节点的 click 状态置为 false
      const clickNodes = this.graph.findAllByState('node', 'click')
      clickNodes.forEach((cn) => {
        this.graph.setItemState(cn, 'click', false)
      })
      const nodeItem = e.item
      // 设置目标节点的 click 状态 为 true
      this.graph.setItemState(nodeItem, 'click', true)
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
        })
      if (nodeItem._cfg.id.startsWith('rp')) {
        this.graph.updateLayout({ type: 'compactBox', direction: 'BT', getHeight: function getHeight () { return 32 }, getVGap: function getVGap () { return 80 } })
      } else {
        this.graph.updateLayout({ type: 'compactBox', direction: 'TB', getVGap: function getVGap () { return 80 } })
      }
      this.title = nodeItem._cfg.model.label
    })
  },
  methods: {
    initG6 () {
      const containerG6 = this.$refs.containerG6
      this.graph = new G6.TreeGraph({
        container: containerG6,
        width: 800,
        height: 650,
        fitView: true,
        fitCenter: true,
        modes: {
          default: ['drag-canvas', 'zoom-canvas', 'drag-node']
        },
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
      })
      this.graph.node(function (node) {
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
            style: {
              // textAlign: 'start'
            }
          }
        }
      })
      this.graph.data(this.result.graph)
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
