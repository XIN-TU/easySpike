
<template>
<div>
  <a-carousel autoplay>
    <div><h3><img src="@/assets/x1.jpg" style="width: 100%;"/></h3></div>
    <div><h3><img src="@/assets/x2.jpg" style="width: 100%;"/></h3></div>
    <div><h3><img src="@/assets/x3.jpg" style="width: 100%;"/></h3></div>
    <div><h3><img src="@/assets/x4.jpg" style="width: 100%;"/></h3></div>
  </a-carousel>

  <div class="Search" >
    <a-input-search placeholder="input your recipe" size="large" @search="onSearch">
      <a-button slot="enterButton">
        Search
      </a-button>
    </a-input-search>
        <a-button @click="hi" type="link" v-trigger >
    </a-button>
  </div>
  <div>
    <a-divider orientation="center" style="font-size: 18px">
      RESULTS
    </a-divider>
    <a-checkbox-group v-model="checkedList" :options="plainOptions" @change="onChange"  />
    <br><br>
    <a-button-group>
      <a-button value='arrow-up' @click="handleSizeChange3">Ready Time <a-icon :type='arrow3' />
      </a-button>
      <a-button value='arrow-up' @click="handleSizeChange1">Num Serving <a-icon :type='arrow1' />
      </a-button>
      <a-button value='arrow-up' @click="handleSizeChange4">Num Want To Try <a-icon :type='arrow4' />
      </a-button>
      <a-button value='arrow-up' @click="handleSizeChange2">Calaries <a-icon :type='arrow2' />
      </a-button>
    </a-button-group>
  </div>
<div>
</div>
  <div class="parent">
      <Recipe v-for="post in currentPosts" v-bind:key="post.id" v-bind="post"></Recipe>
  </div>
  <br/>
  <br/>

  <div id="components-pagination-demo-mini" style="position: relative;margin-top: -60px; height: 60px;clear:both;">
    <a-pagination v-model="current" :total=posts.length show-less-items :page-size="pageSize"
    @showSizeChange="onShowSizeChange"
    @change="changePage"/>
  </div>
</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Recipe from '@/components/Recipe.vue'
import $backend from '../backend'

const plainOptions = ['Quick & Easy', 'Calories<500k', 'Gluten free', 'Vegetarian']
// const defaultCheckedList = ['Apple', 'Orange'];
const defaultCheckedList = []

export default {
  name: 'Search',
  components: {
    HelloWorld,
    Recipe
  },

  data () {
    return {
      checkedList: defaultCheckedList,
      indeterminate: true,
      checkAll: false,
      plainOptions,
      total: 20,
      loading: true,
      // posts: [{}, {}, {}],
      posts: [],
      currentPosts: [],
      error: '',
      // pageSizeOptions: ['5', '10', '15', '20', '50'],
      current: 1,
      pageSize: 6,
      arrow1: 'arrow-up',
      arrow2: 'arrow-up',
      arrow3: 'arrow-up',
      arrow4: 'arrow-up'
    }
  },
  directives: {
    trigger: {
      inserted (el, bingbing) {
        el.click()
      }
    }

  },
  methods: {
    onChange (checkedList) {
      this.indeterminate = !!checkedList.length && checkedList.length < plainOptions.length
      this.checkAll = checkedList.length === plainOptions.length
    },
    handleSizeChange1 (e) {
      this.arrow1 = e.target.value
      if (e.target.value === 'arrow-up') {
        e.target.value = 'arrow-down'
      } else if (e.target.value === 'arrow-down') {
        e.target.value = 'arrow-up'
      }
      console.log(this.arrow1)
      this.onSortServing(e.target.value)
    },
    handleSizeChange2 (e) {
      this.arrow2 = e.target.value
      if (e.target.value === 'arrow-up') {
        e.target.value = 'arrow-down'
      } else if (e.target.value === 'arrow-down') {
        e.target.value = 'arrow-up'
      }
      console.log(this.arrow2)
      this.onSortCalories(e.target.value)
    },
    handleSizeChange3 (e) {
      this.arrow3 = e.target.value
      if (e.target.value === 'arrow-up') {
        e.target.value = 'arrow-down'
      } else if (e.target.value === 'arrow-down') {
        e.target.value = 'arrow-up'
      }
      console.log(this.arrow3)
      this.onSortTime(e.target.value)
    },
    handleSizeChange4 (e) {
      this.arrow4 = e.target.value
      if (e.target.value === 'arrow-up') {
        e.target.value = 'arrow-down'
      } else if (e.target.value === 'arrow-down') {
        e.target.value = 'arrow-up'
      }
      console.log(this.arrow4)
      this.onSortComments(e.target.value)
    },
    // showPage() {
    //   this.currentPosts = this.posts.splice(0, this.pageSize)
    // },
    changePage () {
      var i
      this.currentPosts = []
      console.log(this.current)
      console.log(this.currentPosts.length)
      var index = this.current * this.pageSize
      if (index > this.posts.length) {
        index = this.posts.length
      }
      for (i = (this.current * this.pageSize - this.pageSize); i < index; i++) {
        this.currentPosts.push(this.posts[i])
      }
      console.log(this.currentPosts.length)
      console.log('change it')
    },

    handleClick () {
      this.loading = !this.loading
    },
    hi (value) {
      console.log('chenggong')
      this.posts = []
      value = localStorage.getItem('accessToken')
      console.log(value)
      console.log(this.checkedList)
      this.SearchEnter(value, this.checkedList)
    },
    onSearch (value) {
      this.posts = []
      if (value === '') {
        value = localStorage.getItem('accessToken')
      } else {}
      console.log('test')
      console.log(value)
      console.log(this.checkedList)
      this.SearchEnter(value, this.checkedList)
    },
    // fetchDemo10 () {
    //   $backend
    //     .fetchDemo10()
    //     .then((responseData) => {
    //       console.log(responseData[1])
    //       // temp = JSON.parse(responseData);
    //       console.log('being parsed')
    //       // process the instructions and ingredients

    //       var i
    //       for (i = 0; i < responseData.length; i++) {
    //         var tempInstruction = responseData[i].instructions
    //         var tempIngredients = responseData[i].ingredients
    //         responseData[i].instructions = tempInstruction.split('\n')
    //         responseData[i].ingredients = tempIngredients.split('\n')
    //         // console.log(tempInstruction, tempIngredients);
    //         var j = 0
    //         console.log(responseData[i].ingredients.length)
    //         for (j; j < responseData[i].ingredients.length; j++) {
    //           if (responseData[i].ingredients[j] === 'You might also like') {
    //             break
    //           }
    //         }
    //         responseData[i].ingredients = this.instructions.slice(0, j)
    //         this.posts.push(responseData[i])
    //       }

    //       // this.posts.push(responseData);
    //     })
    //     .catch((error) => {
    //       this.error = error.message
    //     })
    // },
    SearchEnter (keywords, paras) {
      console.log('sent the parameter: ' + keywords + ':' + paras)
      $backend
        .Search(keywords, paras)
        .then((responseData) => {
          console.log('being parsed')
          // process the instructions and ingredients
          var i
          for (i = 0; i < responseData.length; i++) {
            var tempInstruction = responseData[i].instructions
            var tempIngredients = responseData[i].ingredients
            console.log(tempInstruction)
            try {
              // var regexp1 = /(\\r\\n\\r\\n|\\r\\n|\\r\\n\\r)/
              // tempInstruction = tempInstruction.replace(regexp1, '\\t')
              var re = /You might also like\(.|\n\)*/g
              tempInstruction = tempInstruction.replace(re, '')
              responseData[i].instructions = tempInstruction.split('\n')
              responseData[i].ingredients = tempIngredients.split('\n')
            } catch (error) {
              this.error = error.message
              continue
            }
            // console.log(tempInstruction, tempIngredients);
            this.posts.push(responseData[i])
          }
          console.log('initial currentpost')
          this.currentPosts = this.posts.slice(0, this.pageSize)
          // this.posts.push(responseData);
        })
        .catch((error) => {
          this.error = error.message
        })
    },

    DEBUGprint () {
      console.log()
    },
    onShowSizeChange (current, pageSize) {
      this.pageSize = pageSize
    },
    onSortComments (x) {
      function roughScale (x, base) {
        const parsed = parseInt(x, base)
        if (isNaN(parsed)) { return 0 }
        return parsed * 100
      }
      if (x === 'arrow-up') {
        this.posts.sort(function (a, b) {
          a = roughScale(a.comments, 10)
          b = roughScale(b.comments, 10)
          if (a < b) {
            return 1
          } else {
            return -1
          }
        })
      } else if (x === 'arrow-down') {
        this.posts.sort(function (a, b) {
          a = roughScale(a.comments, 10)
          b = roughScale(b.comments, 10)
          if (a > b) {
            return 1
          } else {
            return -1
          }
        })
      }
      // console.log(this.posts[0])
      this.currentPosts = this.posts.slice(0, this.pageSize)
    },
    onSortTime (x) {
      if (x === 'arrow-up') {
        this.posts.sort(function (a, b) {
          var str1 = a.time
          var str2 = b.time
          var list1 = str1.split(' ')
          var list2 = str2.split(' ')
          var num1 = 0
          if (list1.length === 3) {
            if ((list1[2] === 'hours') || (list1[2] === 'hour')) {
              num1 = parseInt(list1[1]) * 60
            } else if ((list1[2] === 'min') || (list1[2] === 'minutes')) {
              num1 = parseInt(list1[1])
            }
          } else {
            num1 = parseInt(list1[1]) * 60 + parseInt(list1[3])
          }
          var num2 = 0
          if (list2.length === 3) {
            if ((list2[2] === 'hours') || (list2[2] === 'hour')) {
              num2 = parseInt(list2[1]) * 60
            } else if ((list2[2] === 'min') || (list2[2] === 'minutes')) {
              num2 = parseInt(list2[1])
            }
          } else {
            num2 = parseInt(list1[2]) * 60 + parseInt(list1[2])
          }
          if (num1 < num2) {
            return 1
          } else {
            return -1
          }
        })
      } else if (x === 'arrow-down') {
        this.posts.sort(function (a, b) {
          var str1 = a.time
          var str2 = b.time
          var regexp = /[0-9]+/g
          var list1 = str1.match(regexp)
          var list2 = str2.match(regexp)
          var num1 = 0
          if (list1.length === 3) {
            if (list1[2] === 'hours') {
              num1 = parseInt(list1[1]) * 60
            } else if ((list1[2] === 'min') || (list1[2] === 'minutes')) {
              num1 = parseInt(list1[1])
            }
          } else {
            num1 = parseInt(list1[1]) * 60 + parseInt(list1[3])
          }
          var num2 = 0
          if (list2.length === 3) {
            if (list2[2] === 'hours') {
              num2 = parseInt(list2[1]) * 60
            } else if ((list2[2] === 'min') || (list2[2] === 'minutes')) {
              num2 = parseInt(list2[1])
            }
          } else {
            num2 = parseInt(list1[2]) * 60 + parseInt(list1[2])
          }
          if (num1 > num2) {
            return 1
          } else {
            return -1
          }
        })
      }
      // console.log(this.posts[0])
      this.currentPosts = this.posts.slice(0, this.pageSize)
    },
    onSortServing (x) {
      function roughScale (x, base) {
        const parsed = parseInt(x, base)
        if (isNaN(parsed)) { return 0 }
        return parsed * 100
      }
      if (x === 'arrow-up') {
        this.posts.sort(function (a, b) {
          console.log(a.serving)
          a = roughScale(a.serving, 10)
          b = roughScale(b.serving, 10)
          if (a < b) {
            return 1
          } else {
            return -1
          }
        })
      } else if (x === 'arrow-down') {
        this.posts.sort(function (a, b) {
          a = roughScale(a.serving, 10)
          b = roughScale(b.serving, 10)
          if (a > b) {
            return 1
          } else {
            return -1
          }
        })
      }
      // console.log(this.posts[0])
      this.currentPosts = this.posts.slice(0, this.pageSize)
    },
    onSortCalories (x) {
      function roughScale (x, base) {
        const parsed = parseInt(x, base)
        if (isNaN(parsed)) { return 0 }
        return parsed * 100
      }
      if (x === 'arrow-up') {
        this.posts.sort(function (a, b) {
          let num1 = a.calories.replace(/[^\d.]/g, '')
          let num2 = b.calories.replace(/[^\d.]/g, '')
          a = roughScale(num1, 10)
          b = roughScale(num2, 10)
          if (a < b) {
            return 1
          } else {
            return -1
          }
        })
      } else if (x === 'arrow-down') {
        this.posts.sort(function (a, b) {
          let num1 = a.calories.replace(/[^\d.]/g, '')
          let num2 = b.calories.replace(/[^\d.]/g, '')
          a = roughScale(num1, 10)
          b = roughScale(num2, 10)
          if (a > b) {
            return 1
          } else {
            return -1
          }
        })
      }
      // console.log(this.posts[0])
      this.currentPosts = this.posts.slice(0, this.pageSize)
    }
  }
}

</script>

<style lang="scss" scoped>

#components-pagination-demo-mini .ant-pagination:not(:last-child) {
  margin-bottom: 24px;}

//  .parent{display:flex;align-items:center;}

.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 160px;
  line-height: 160px;
  background: #364d79;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide h3 {
  color: #fff;
}
</style>
