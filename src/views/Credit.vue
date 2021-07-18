/* eslint-disable */

<template>
  <div class="credit">
    <div class="aspect-ratio">
      <!-- <iframe src="//player.bilibili.com/player.html?aid=53851218&bvid=BV1j4411W7F7&cid=94198756&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height='600px' width='800px'> </iframe> -->

      <!-- This below is a sample recipe for {{ title }}. <br />
      <br /> -->

      <!-- <HelloWorld msg="Project Information"/> -->
      <!-- <Recipe msg="Project Information"/> -->
          <a-input-search allowClear=True placeholder="input your recipe" size="large" @search="onSearch">
      <a-button slot="enterButton" v-on:click="DEBUGprint">
        Search
      </a-button>
    </a-input-search>
      <a href="" @click.prevent="fetchDemo10">Fetch</a><br />
      <a href="" @click.prevent="pushSearchKeys">Push</a><br />

      <Recipe v-for="post in posts" v-bind:key="post.id" v-bind="post">
      </Recipe>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Recipe from '@/components/Recipe.vue'
import $backend from '../backend'

export default {
  name: 'credit',
  components: {
    HelloWorld,
    Recipe
  },

  data: function () {
    return {
      posts: [],
      error: ''
    }
  },
  methods: {
    onSearch (value) {
      console.log(value)
    },

    fetchDemo10 () {
      $backend
        .fetchDemo10()
        .then((responseData) => {
          console.log(responseData[1])
          // temp = JSON.parse(responseData);
          console.log('being parsed')
          // process the instructions and ingredients

          var i
          for (i = 0; i < responseData.length; i++) {
            var tempInstruction = responseData[i].instructions
            var tempIngredients = responseData[i].ingredients
            responseData[i].instructions = tempInstruction.split('\n')
            responseData[i].ingredients = tempIngredients.split('\n')
            // console.log(tempInstruction, tempIngredients);

            this.posts.push(responseData[i])
          }

          // this.posts.push(responseData);
        })
        .catch((error) => {
          this.error = error.message
        })
    },
    pushSearchKeys () {
      $backend
        .pushSearchKeys()
      console.log('send the parameter')
    },

    DEBUGprint () {
      console.log()
    }

  }
}
</script>

<style lang="scss">
/* 这个规则规定了iframe父元素容器的尺寸，我们要去它的宽高比应该是 25:14 */
.aspect-ratio {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 60%; /* 高度应该是宽度的56% */
}
/* 设定iframe的宽度和高度，让iframe占满整个父元素容器 */
.aspect-ratio iframe {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
}
</style>
