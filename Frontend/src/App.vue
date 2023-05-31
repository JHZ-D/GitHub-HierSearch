<template>
  <n-layout style="height: 100vh;">
    <n-layout-sider
      style="z-index: 1;"
      bordered
      show-trigger
      collapse-mode="width"
      :collapsed-width="80"
      :width="280"
      :collapsed="collapsed"
      @collapse="collapsed = true"
      @expand="collapsed = false"
    >
      <n-menu
        :collapsed="collapsed"
        :collapsed-width="80"
        :collapsed-icon-size="24"
        :items="menuItems"
        @update:value="menuCallback"
      />
    </n-layout-sider>
    <n-layout class="app-content">
        <n-message-provider>
          <n-notification-provider>
            <router-view v-slot="{Component}">
              <keep-alive>
                <component :is="Component"/>
              </keep-alive>
            </router-view>
          </n-notification-provider>
        </n-message-provider>
    </n-layout>
  </n-layout>
</template>

<script>
import { defineComponent, h } from 'vue'
import { NIcon } from 'naive-ui'
import { mapActions, mapState } from 'vuex'
import {
  HomeOutline as HomeIcon,
  BookOutline as BookIcon,
  SearchOutline as SearchIcon
} from '@vicons/ionicons5'

function renderIcon (icon) {
  return () => h(NIcon, null, { default: () => h(icon) })
}

export default defineComponent({
  data () {
    return {
      collapsed: true,
      menuItems: [
        {
          label: '主页',
          key: 'home',
          icon: renderIcon(HomeIcon)
        },
        {
          label: '层次化学习系统',
          key: 'section',
          icon: renderIcon(BookIcon)
        },
        {
          label: '层次化检索系统',
          key: 'search',
          icon: renderIcon(SearchIcon)
        }
      ]
    }
  },
  methods: {
    menuCallback (value, item) {
      if (value === 'home') {
        this.$router.push('/')
      } else if (value === 'search') {
        this.$router.push('/search')
      } else if (value === 'section') {
        this.$router.push('/section')
      }
    },
    handleScroll (e) {
      console.log(e.currentTarget)
      const scrollContainer = e.currentTarget
      console.log('scrollTop', scrollContainer.scrollTop)
      console.log('scrollHeight', scrollContainer.scrollHeight)
      console.log('offsetHeight', scrollContainer.offsetHeight)
    },
    ...mapActions({
      onCoolClick: 'hello_homura'
    })
  },
  computed: {
    ...mapState({
      coolButtonText: 'hello',
      en: 'en'
    })
  }
})
</script>

<style>
.n-menu-item {
  margin: 20px 0;
}
</style>
