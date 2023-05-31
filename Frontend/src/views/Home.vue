<template>
  <div class="home">
    <n-tooltip trigger="hover">
      <template #trigger>
        <n-button ghost circle size="large" @click="showModal = true" id="home-help-btn"><n-icon size="30" color="#cde6c7"><HelpIcon/></n-icon></n-button>
      </template>
      帮助
    </n-tooltip>
    <n-tooltip trigger="hover">
      <template #trigger>
        <n-button ghost circle size="large" @click="showContact = true" id="home-contact-btn"><n-icon size="30" color="#cde6c7"><MailIcon/></n-icon></n-button>
      </template>
      联系我们
    </n-tooltip>
        <a href="https://github.com/JHZ-D/Wikipedia-graph-constructor" target="_blank">
    <n-tooltip trigger="hover">
      <template #trigger>
          <n-button ghost circle size="large" id="home-source-btn"><n-icon size="30" color="#cde6c7"><SourceIcon/></n-icon></n-button>
      </template>
      开源地址
    </n-tooltip>
        </a>
    <n-space vertical>
      <h1
        id="project-name"
        ref="name"
        >
        <!-- PROJECT {{heroine}} -->
        GITHUB HIER-SEARCH
      </h1>
      <!-- <n-h6>{{en?"A":"一个"}} JAVADOC API {{en?" learning assistant system ":"学习助手服务"}}</n-h6>
      <p id="section-nav" class="home-p">{{en?"Start learn! From recommended ":"如果你是小白、不知从哪开始学，可以看看我们推荐的"}}<router-link class="link" to="/section"><n-gradient-text type="info">{{en?"learning entries":"学习入口"}}
      </n-gradient-text></router-link></p>
      <h2 class="home-h">{{en?"OR":"如果你想自己看看"}}</h2>
      <p class="home-p">{{en?"":"可以用任何你想到的词来"}}<router-link class="link" to="/search"><n-gradient-text type="info">{{en?"Search APIs":"搜索API"}}</n-gradient-text></router-link>{{en?" you're interested in":""}}</p> -->
      <h2 class="home-p">基于Wikipedia软件开发领域的层级知识图谱</h2>
      <h2 class="home-p">和Github Topic的层次结构的Github层次化学习与检索服务</h2>
      <div id="search-container" style="width: fit-content; margin: 100px auto;">
        <n-dropdown @select="handleSearchSelect" trigger="click" :options="searchTypeOptions">
          <n-button :keyboard="false" id="search-choose">{{repo?"搜索仓库":"搜索知识点"}}</n-button>
        </n-dropdown>
        <MultiSearchBread @receive="getMsg" v-if="repo" style="order: 2; background-color: rgba(240, 248, 255, 0.9); padding: 10.333px 0; border-top:1px solid rgba(224, 224, 224, 1); border-bottom:1px solid rgba(224, 224, 224, 1)"></MultiSearchBread>
        <div id="search-space">
          <n-auto-complete
            id="search-input"
            :options="searchOptions"
            v-model:value="searchValue"
            size="large"
            :placeholder="repo?'输入仓库':'输入知识点，如Software development, Java, Spring, vue...'"
            :get-show="getShow"
          />
          <n-button circle @click="onSearchClick">
            <template #icon>
              <n-icon color="#cde6c7"><SearchIcon /></n-icon>
            </template>
          </n-button>
        </div>
      </div>
    </n-space>
    <n-modal v-model:show="showModal">
      <n-card style="max-width: 1200px; " :title="如何使用" :bordered="false" size="huge">
        <div>
          <p>本系统为Github层次化学习与检索系统，由层次化学习系统和层次化检索系统组成。您可以点击搜索框左边的下拉框选择搜索知识点或搜索仓库。</p>
          <p>选择搜索知识点，您可以搜索Wikipedia软件开发领域的知识或Github Topic代表的知识，从而进入Github层次化学习系统。</p>
          <p>选择搜索仓库，您可以搜索Github上的仓库，从而进入Github层次化检索系统。</p>
          <p>您也可以通过页面左侧导航进入学习系统或检索系统。</p>
          <n-button
            @click="handleButtonClick"
          >
            确定
          </n-button>
        </div>
        <!-- <n-steps :current="current" status="process">
          <n-step :title="en?'Find an API to learn':'首先寻找要学习的API'">
            <div class="n-step-description">
              <p v-if="en">Choose one API to start your learn journey~ If you are a complete novice, don't know where to start, you can browse some popular <router-link class="link" to="/section"><n-gradient-text type="info">Learning Entries</n-gradient-text></router-link> we prepare for you and find out what you interested in.</p>
              <p v-else>万事开头难！要学习API文档中的海量API，第一步就必须要先选择几个API来学起来。如果你真的是个新手，觉得API太多头大、不知从哪开始，不妨看看我们推荐的<router-link class="link" to="/section"><n-gradient-text type="info">学习入口</n-gradient-text></router-link>；每个学习入口都包含几个API，这些API涉及java的不同主题、非常常用而且开发者们很关注它们。</p>
              <p v-if="en">Or, you can search for java APIs with any keywords you come up with in the <router-link class="link" to="/search"><n-gradient-text type="info">Search Page</n-gradient-text></router-link> to find out APIs which meet your need</p>
              <p v-else>或者如果你有一些java基础，想了解一下自己感兴趣的一些领域（比如网络通信、多线程、IO等），你可以访问我们的<router-link class="link" to="/search"><n-gradient-text type="info">搜索页面</n-gradient-text></router-link>。在这里可以用你想得到的各种关键词搜索到你可能有兴趣的API，保证比javadoc的搜索靠谱（大概</p>
              <n-button
                v-if="current === 1"
                @click="handleButtonClick"
              >
                {{en?"Next":"下一步"}}
              </n-button>
            </div>
          </n-step>
          <n-step :title="en?'Learn the API you choose in the Roadmap':'在路线图中学习你选择的API'">
            <div class="n-step-description">
              <p v-if="!en">API学习从来都不是单打独斗，实际开发中、往往需要配合使用一系列的API来完成你的编程任务。在学习中，围绕一个具体的主题、学习<n-gradient-text type="error">一组</n-gradient-text>关系密切的API、理解它们之间的关系、往往效率更高。</p>
              <p v-if="en">The API you choose in the first step are set as the center API of our <router-link class="link" to="/roadmap"><n-gradient-text type="info">Roadmap</n-gradient-text></router-link>. Through the Roadmap, you can browse the relationships between the API you choose and all other APIs which are related to it. You can also navigate in the Roadmap to continue learning other related APIs. <router-link class="link" to="/roadmap"><n-gradient-text type="info">Check it Out!</n-gradient-text></router-link></p>
              <p v-else>我们的服务使用<router-link class="link" to="/roadmap"><n-gradient-text type="info">API路线图</n-gradient-text></router-link>来帮你快速找到和所选API关系密切的一系列API。API路线图是一张以图结构组织起来的API的网，图中的结点就是各个API，结点间以边相连，边上标注了API之间的关系。通过路线图，你能够浏览所有API之间的关系、轻易找出应该重点学习的API，并在路线图上规划自己的学习路径。</p>
              <n-button
                v-if="current === 2"
                @click="handleButtonClick"
              >
                {{en?"Next":"下一步"}}
              </n-button>
            </div>
          </n-step>
          <n-step :title="en?'Learn Stack Overflow threads about the API':'在最著名的开发者社区Stack Overflow中学习API知识！'">
            <div class="n-step-description">
              <p v-if="en">While navigating in the Roadmap,you can further browse popular Stack Overflow threads which are talking about the current API you learn. These valuable threads can help you better learn the API in the real development scenario. Good Luck. :-) <router-link class="link" to="/detail"><n-gradient-text type="info">Try it out</n-gradient-text></router-link></p>
              <p v-else>Stack Overflow是世界最知名的开发者Q&A社区，其中包含了大量开发者针对API在实际开发场景下的讨论，有很大的学习价值。对每个API，我们都收集了几乎全部在Stack Overflow社区中对其进行的讨论，您可以在通过路线图查看API的同时对所有该API相关的讨论进行学习。相信这对你了解API的使用方法有很大帮助，祝你好运！:-)</p>
              <n-button
                v-if="current === 3"
                @click="handleButtonClick"
              >
                {{en?"Understand":"明白了"}}
              </n-button>
            </div>
          </n-step>
        </n-steps> -->
      </n-card>
    </n-modal>
    <n-modal v-model:show="showContact">
      <n-card style="max-width: 1200px; " :title="联系方式" :bordered="false" size="huge">
        <div>
          <p>电话：13321132034</p>
          <p>邮箱：1336024978@qq.com</p>
          <n-button
            @click="handleButtonClickContact"
          >
            确定
          </n-button>
        </div>
      </n-card>
    </n-modal>
  </div>
</template>

<script>
// @ is an alias to /src
import { defineComponent } from 'vue'
import { mapState, mapMutations } from 'vuex'
import { Help as HelpIcon, SearchOutline as SearchIcon, Mail as MailIcon, LogoGithub as SourceIcon } from '@vicons/ionicons5'
import axios from 'axios'
import MultiSearchBread from '../components/MultiSearchBread.vue'
import words from '@/assets/labelset.json'
import knowpdict from '@/assets/knowpdict.json'

// let showed = false

export default defineComponent({
  name: 'Home',
  components: {
    HelpIcon,
    SearchIcon,
    MailIcon,
    SourceIcon,
    MultiSearchBread
  },
  data () {
    return {
      searchValue: '',
      current: 1,
      showModal: false,
      showContact: false,
      words: words,
      knowpdict: knowpdict,
      chosenCate: '',
      objArr: [],
      searchTypeOptions: [
        {
          label: '搜索知识点',
          key: 'know'
        },
        {
          label: '搜索仓库',
          key: 'repo'
        }
      ]
    }
  },
  // mounted () {
  //   if (!showed) {
  //     showed = true
  //     this.showModal = true
  //   }
  // },
  methods: {
    getMsg (data) {
      this.chosenCate = data.chosenCate
      this.objArr = data.objArr
    },
    async onSearchClick () {
      if (this.repo === true) {
        axios.get('/repo', { params: { text: this.searchValue, cate: this.chosenCate } })
          .then(res => {
            // res.data是后端传回来的结果，假设是一个数组
            // 使用路由跳转到新页面，并把结果作为参数传递
            this.$router.push({ path: '/search', query: { data: JSON.stringify(res.data.repos), objArr: this.objArr, searchText: this.searchValue } })
          })
      } else {
        if (this.searchValue === '') {
          return
        }
        axios.get('/getKnowp', { params: { text: this.knowpdict[this.searchValue] } })
        // 在发送用户输入的文本给后端后，接收后端传回来的结果
        // axios.get('/getKnowp', { params: { text: ':S' + this.searchValue } })
          .then(res => {
            // res.data是后端传回来的结果，假设是一个数组
            // 使用路由跳转到新页面，并把结果作为参数传递
            this.$router.push({ path: '/section', query: { graph: JSON.stringify(res.data.graph), description: res.data.description, url: res.data.url, title: this.searchValue } })
            // this.$router.push({ name: 'Section', params: { data: res.data } })
          })
      }
      // const paramObj = {
      //   query: this.searchValue
      // }
      // const literalRes = await this.$http.post(this.loadUrl, paramObj)
      // const literalData = literalRes.data.data
      // this.literal_items = literalData
      // this.messageBox.success('thread info list loaded', { duration: 500 })
    },
    handleLangSelect (key) {
      this.set_language(key)
    },
    handleSearchSelect (key) {
      this.set_searchtype(key)
    },
    handleButtonClick () {
      // if (this.current === 3) {
      //   this.showModal = false
      // } else {
      //   this.current = (this.current % 3) + 1
      // }
      this.showModal = false
    },
    handleButtonClickContact () {
      // if (this.current === 3) {
      //   this.showModal = false
      // } else {
      //   this.current = (this.current % 3) + 1
      // }
      this.showContact = false
    },
    ...mapMutations({
      set_language: 'set_language',
      set_searchtype: 'set_searchtype'
    })
  },
  computed: {
    searchOptions () {
      // const words = ['apple', 'banana', 'carrot', 'date', 'eggplant', 'Software development']
      if (this.repo === true) {
        return []
      }
      const words = this.words
      const prefix = this.searchValue
      return words.filter(word => word.toLocaleLowerCase().startsWith(prefix.toLocaleLowerCase())).map(word => {
        return {
          label: word,
          value: word
        }
      })
      // return ['没做完', '是真的', '别想了'].map((suffix) => {
      //   const prefix = this.searchValue.split('@')[0]
      //   return {
      //     label: prefix + suffix,
      //     value: prefix + suffix
      //   }
      // })
    },
    ...mapState({
      en: 'en',
      repo: 'repo'
    })
  }
})
</script>

<style scope>
.home {
  text-align: center;
  background: url("../assets/backgd5.jpg");
  width: 100%;
  height: 100%;
  background-size: cover;
}

#project-name {
  margin-top: 50px;
  /* color: #F1394B; */
  color: #fedcbd;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: 900;
  font-size: 600%;
}

#section-nav .link {
  font-weight: bold;
  color: #2c3e50;
}

#section-nav a.router-link-exact-active {
  color: #42b983;
}

#search-space {
  /* display: flex;
  justify-content: center; */
  order: 3; /* move it to the left */
}

#search-input {
  width: 550px;
  display: inline-block;
  margin-right: 20px;
}

#home-help-btn {
  /* position: absolute; */
  /* top: 0;
  left: 0;
  margin: 20px; */
  position: fixed; /* position relative to the viewport */
  bottom: 50px;
  left: 20%;
  margin: 50px;
}

#home-contact-btn {
  /* position: absolute;
  bottom: 50px;
  left: 100px;
  margin: 50px; */
  position: fixed; /* position relative to the viewport */
  bottom: 50px; /* set at the bottom edge of the viewport */
  left: 50%; /* set at the horizontal center of the viewport */
  transform: translateX(-100%);
  margin: 50px; /* add some space around the element */
}

#home-source-btn {
  /* position: absolute;
  bottom: 50px;
  left: 100px;
  margin: 50px; */
  position: fixed; /* position relative to the viewport */
  bottom: 50px; /* set at the bottom edge of the viewport */
  right: 20%; /* set at the horizontal center of the viewport */
  margin: 50px; /* add some space around the element */
}

#lang-choose {
  position: absolute;
  top: 0;
  right: 0;
  margin: 20px;
}

#search-choose {
  /* position: absolute;
  top: 0;
  right: 0;
  margin: 20px; */
  order: 1; /* move it to the right */
  width: 100px;
  height: 40px;
  background-color: rgb(240, 248, 255);
  /* color: red; */
}

#search-container {
  display: flex; /* make it a flex container */
  flex-direction: row; /* arrange the items horizontally */
  justify-content: center; /* center the items along the main axis */
  align-items: center; /* center the items along the cross axis */
  margin-top: 100px; /* add 50 pixels of space above the element */
  /* background-color: rgba(255, 255, 255, 0.5); */
}

/* #confirm-button {
  position: absolute;
  right: 50%;
} */

/* #search-choose {
}

#search-space {
} */

.home-p {
  font-size: x-large;
  font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: bolder;
  color: #afb4db;
}

.home-h {
  font-size: xx-large;
  font-weight: 900;
}
</style>
