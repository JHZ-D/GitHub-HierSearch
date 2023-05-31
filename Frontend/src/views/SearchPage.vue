<template>
  <div class="search-page">
    <n-space vertical size="large" class="space-back">
      <div style="background-color: rgba(255, 255, 255, 0.1);">
        <n-layout>
          <n-layout-header bordered id="header" style="background-color: rgba(175, 223, 228,0.9);">
            <n-space id="head-space" size="huge" align="baseline">
              <n-h1>Github层次化检索系统</n-h1>
                <n-tooltip trigger="hover">
                  <template #trigger>
                    <n-button ghost circle size="small" @click="showModal = true"><n-icon
                    size="20"><help-icon /></n-icon></n-button>
                  </template>
                  帮助
                </n-tooltip>
            </n-space>
          </n-layout-header>
        </n-layout>
          <!-- <n-layout-content class="headerasearch" style="background-color: rgba(144, 215, 236,0.7);"> -->
            <div id="search-container">
              <MultiSearchBread @receive="getMsg" :info="objArr"></MultiSearchBread>
              <div id="search-space">
                <n-auto-complete
                    id="search-input"
                    v-model:value="searchValue"
                    size="large"
                    placeholder="搜索仓库"
                />
                <n-button circle @click="onSearchClick">
                  <template #icon>
                    <n-icon><Search /></n-icon>
                  </template>
                </n-button>
              </div>
            </div>
          <!-- </n-layout-content> -->
      </div>
      <!-- <div class="card">
        <n-card title="搜索结果" size="huge" style="background-color:rgba(255, 255, 255,0.2);">
          <n-grid :x-gap="12" :y-gap="8" :cols="4">
            <n-grid-item v-for="num in repodata.length" :key="num">
              <a :href="'https://github.com/'+repodata[num - 1]" target="_blank">
                <div :class="num % 2 === 0 ? 'light-green' : 'green'">{{ repodata[num - 1] }}</div>
              </a>
            </n-grid-item>
          </n-grid>
        </n-card>
      </div> -->
  <n-data-table style="height: 500px; width: 1200px; margin: 50px auto; --td-padding: 10px; --th-padding: 11px" :columns="columns" :data="repodata" :pagination="pagination" flex-height><n-empty description="找不到符合条件的仓库！">
  </n-empty></n-data-table>
    </n-space>
  </div>
  <n-modal v-model:show="showModal">
          <n-card style="width: 600px;" title="如何使用" :bordered="false"
            size="huge">
            <p>您可以在搜索框左侧逐层选择与自己感兴趣内容最相关的topic，从而逐步发掘自己的需求。</p>
            <p>选定topic后，在搜索框中输入想要搜索的内容，点击搜索按钮，就可以得到相关topic下的有关仓库。</p>
          </n-card>
        </n-modal>
</template>

<script>
import { h, defineComponent, reactive } from 'vue'
import { Search, TrashOutline, Help as HelpIcon } from '@vicons/ionicons5'
import { mapState, mapMutations } from 'vuex'
import axios from 'axios'
import MultiSearchBread from '../components/MultiSearchBread.vue'
// import repodata from '@/assets/midrepos.json'

// const tableData = Array.from(repodata).map((item, index) => ({
//   key: index,
//   reponame: item
// }))
const columns = [
  {
    title: 'Repository',
    width: 350,
    key: 'reponame',
    render (row, index) {
      return h('a', { href: 'https://github.com/' + row.reponame, target: '_blank' }, row.reponame) // <a href="'https://github.com/'+repodata[index - 1]" target="_blank">{{ repodata[num - 1] }}</a>
    }
  },
  {
    title: 'Description',
    width: 840,
    key: 'description'
  }
]

export default defineComponent({
  components: {
    Search,
    // MultilevelSelecter
    MultiSearchBread,
    HelpIcon
  },
  data () {
    return {
      searchValue: '',
      messageBox: undefined,
      literal_items: [],
      showModal: false,
      repodata: [],
      result: [],
      objArr: [],
      searchText: '',
      chosenCate: '0'
    }
  },
  created () {
    this.$watch('chosenCate', (newValue, oldValue) => {
      // 执行相应的函数
      if (this.searchValue === '' && this.chosenCate === '0') {
        return
      }
      axios.get('/repo', { params: { text: this.searchValue, cate: newValue } })
        .then(res => {
          this.repodata = res.data.repos
        })
    })
    this.objArr = this.$route.query.objArr
  },
  mounted () {
    // 获取参数并赋值给result
    if (this.$route.query.data === undefined) {
      return
    }
    this.repodata = JSON.parse(this.$route.query.data)
    this.searchValue = this.$route.query.searchText
  },
  setup () {
    const paginationReactive = reactive({
      page: 1,
      pageSize: 10,
      // showSizePicker: true,
      // pageSizes: [3, 5, 7],
      onChange: (page) => {
        paginationReactive.page = page
      },
      onUpdatePageSize: (pageSize) => {
        paginationReactive.pageSize = pageSize
        paginationReactive.page = 1
      }
    })
    return {
      columns,
      pagination: paginationReactive
    }
  },
  methods: {
    getMsg (data) {
      this.chosenCate = data.chosenCate
      this.objArr = data.objArr
    },
    async onSearchClick () {
      if (this.searchValue === '') {
        return
      }
      axios.get('/repo', { params: { text: this.searchValue, cate: this.chosenCate } })
        .then(res => {
          this.repodata = res.data.repos
        })
      // const paramObj = {
      //   query: this.searchValue
      // }
      // const literalRes = await this.$http.post(this.loadUrl, paramObj)
      // const literalData = literalRes.data.data
      // this.literal_items = literalData
      // this.messageBox.success('thread info list loaded', { duration: 500 })
    },
    onViewClick (item) {
      this.set_id(item.id)
      this.set_section_id('')
      this.update_map(TrashOutline)
      this.set_show_map(false)
      this.$router.push('/roadmap')
    },
    ...mapMutations({
      set_id: 'set_current_center_node',
      set_section_id: 'set_current_section_id',
      set_show_map: 'set_map_show_mode',
      update_map: 'set_refresh_map'
    })
  },
  computed: {
    loadUrl () {
      return '/search/' + this.docName
    },
    loadConceptUrl () {
      return '/searchByConcept/' + this.docName
    },
    ...mapState({
      docName: 'doc_name',
      en: 'en'
    })
  }
})
</script>

<style>
#search-container {
    display: flex;
    justify-content: center;
    align-items: center;
    align-content: space-between;
    margin-top: 20px;
    margin-bottom: 5px;
    /* width: 50%; */
}

#head-space{
  height:50px !important;
  margin-top: 0 !important;
}
.card {
  padding: 10px;
  word-break: break-all;
  width: 80%;
  height: 80%;
  border-radius: 5px;
  box-shadow: 0px 0px 5px #888888;
  margin-bottom: 20px;
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 2%;
  /* background-color: blueviolet;
  color: aquamarine; */
}

.light-green {
  height: 90px;
  background-color: rgba(0, 128, 0, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
}
.green {
  height: 90px;
  background-color: rgba(0, 128, 0, 0.24);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* #search-space {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    background-size: cover;
} */

.search-page {
  /* background: url("../assets/backgd1.jpg"); */
  background-image: linear-gradient(white, #7bbfea);

  width: 100%;
  height: 100%;
  background-size: cover;
  background-attachment:fixed;
}

/* .space-back {
  background: url("../assets/backgd.jpg");
  background-size: cover;
  background-attachment:fixed;
  margin-bottom: 0;
} */

.headerasearch {
  background-color:rgba(220,38,38,0.2);
  /* margin-top: -10px; */
}
</style>
