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
        GITHUB HIER-SEARCH
      </h1>
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
          })
      }
    },
    handleLangSelect (key) {
      this.set_language(key)
    },
    handleSearchSelect (key) {
      this.set_searchtype(key)
    },
    handleButtonClick () {
      this.showModal = false
    },
    handleButtonClickContact () {
      this.showContact = false
    },
    ...mapMutations({
      set_language: 'set_language',
      set_searchtype: 'set_searchtype'
    })
  },
  computed: {
    searchOptions () {
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
  order: 3; /* move it to the left */
}

#search-input {
  width: 550px;
  display: inline-block;
  margin-right: 20px;
}

#home-help-btn {
  position: fixed; /* position relative to the viewport */
  bottom: 50px;
  left: 20%;
  margin: 50px;
}

#home-contact-btn {
  position: fixed; /* position relative to the viewport */
  bottom: 50px; /* set at the bottom edge of the viewport */
  left: 50%; /* set at the horizontal center of the viewport */
  transform: translateX(-100%);
  margin: 50px; /* add some space around the element */
}

#home-source-btn {
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
