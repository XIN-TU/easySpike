<template>
  <div id="app">
    <!-- <div id="nav">
    </div> -->

  <a-layout id="components-layout-demo-fixed-sider">
    <a-layout-sider :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0 }"  v-model="collapsed" collapsible>
      <div class="logo">
        <img src="@/assets/gordon.png" width=100%>
      </div>
      <a-menu theme="dark" mode="inline" :default-selected-keys="['1']">
        <a-menu-item key="1">
          <a-icon type="home"  />
          <span class="nav-text">Home</span>
          <router-link to="/">Info</router-link>
        </a-menu-item>
        <a-menu-item key="2">
          <a-icon type="search" />
          <span class="nav-text">Search</span>
          <router-link to="/search">Search</router-link>
        </a-menu-item>
        <a-menu-item key="3">
          <a-icon type="api" />
          <span class="nav-text">API</span>
          <router-link to="/api">API Sample</router-link>
        </a-menu-item>

      <!-- <router-link to="/">Info</router-link> |
      <router-link to="/search">Search</router-link> |
      <router-link to="/api">API Sample</router-link> -->

      </a-menu>
    </a-layout-sider>
    <a-layout :style="{ marginLeft: '200px' }">
      <a-layout-header :style="{ background: '#fff', padding: 0, textAlign: 'center' }"  >
        <h2>
             Simple Recipe Search Engine
        </h2>
      </a-layout-header>

      <a-layout-footer :style="{ textAlign: 'center' }">
        Ant Design ©2018 Created by Ant UED
      </a-layout-footer>
    </a-layout>
  </a-layout>

  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #00839b;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 50px;
  vertical-align: top;
  line-height: 100px;
}
</style>
