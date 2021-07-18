<template>
  <div class="recipe_entry" style="width:50%; float:left; margin: 0; padding: 0">
    <!-- <h1>{{ msg }}</h1> -->
      <a-card :loading="loading" :title="title" :hoverable="true">
      <!-- <a slot="extra" href="#">More</a> -->
      <div style="margin: 0; padding: 0">
        <div style="width: 40%; float: left; margin: 0; padding: 0">
          <p>
            <img :src="img_link" width="100%" height="280px" />
          </p>
        </div>

        <div style="width: 50%; float: left; margin: 0; padding: 0;">
          <br/>
          <p class="ab"><a-icon type="clock-circle" theme="twoTone" two-tone-color="#73d13d"  /> {{ time }}</p>
          <br/>
          <p class='ab'><a-icon type="smile" theme="twoTone" two-tone-color="#40a9ff" /> {{ serving }}</p>
          <br/>
          <p class="ab"><a-icon type="heart" theme="twoTone" two-tone-color="#ff4d4f" /> {{ comments }}</p>
          <br/>
          <p class="ab"><a-icon type="fire" theme="twoTone" two-tone-color="#ffa940" /> {{ calories }}</p>
          <br/>
        </div>
          <!-- <a-list
            size="small"
            bordered
            :data-source="notes"
            style="width: 90%; margin-top: 10%; margin-left: 2%"
          >
            <a-list-item
              slot="renderItem"
              slot-scope="item"
              style="text-align: left"
            >
              {{ item }}
            </a-list-item>
            <div slot="header">Notes</div>
          </a-list> -->
        <div style="width: 100%; float: left; margin: 0; padding: 0">
          <a-collapse  @change="changeActivekey" >
            <a-collapse-panel key="1" header="INGREDIENTS" :show-arrow="false" style="font-weight:bold;">
              <a-card style="width: 100%">
              <div>
              <a-list size="small" bordered :data-source="ingredients">
                <a-list-item
                  slot="renderItem"
                  slot-scope="item"
                  style="text-align: left"
                >
                  {{ item }}
                </a-list-item>
                <!-- <div slot="header">INGREDIENTS</div> -->
              </a-list>
            </div>
          </a-card>
      </a-collapse-panel>
      <a-collapse-panel
        key="2"
        header="INSTRUCTIONS"
        :show-arrow="false"
        style="font-weight:bold;"
      >
        <a-card style="width: 100%">
            <div >
              <a-list size="small" bordered :data-source="instructions">
                <a-list-item
                  slot="renderItem"
                  slot-scope="item"
                  style="text-align: left"
                >
                  {{ item }}
                </a-list-item>
                <!-- <div slot="header">INSTRUCTIONS</div> -->
              </a-list>
            </div>
          </a-card>
        </a-collapse-panel>
        </a-collapse>
      </div>
      </div>
    </a-card>
    <!-- FOR BETTER SPACING -->
    <br />
    <br />
  </div>
</template>

<script>
// const plainOptions = [
//   'Quick & Easy',
//   'Calaries<500k',
//   'Gluten free',
//   'Vegetarian'
// ]
// const defaultCheckedList = ['Apple', 'Orange'];
// const defaultCheckedList = []

// const ingredients = [
//   '1/2 cn Pillsbury Cream Cheese Frosting ',
//   '2 oz Vanilla-Flavored Candy ',
//   '14 Creme-Filled Chocolate Cookies ',
//   'Orange Food Coloring ',
//   '7 sm Green Gumdrops cut in half',
//   '1 Tube Decorator Icing '
// ]

// const instructions = [
//   '1. In small saucepan, combine frosting and candy coating; melt over low  heat, stirring occasionally until smooth.  Remove from heat.  Stir in desired amount of food color.',
//   '2. Line cookie sheets with waxed paper. Using tongs, dip each cookie in  melted frosting mixture, coating completely. Lay flat on cookie sheets. Let  stand 10 minutes until set.',
//   '3. Decorate coated cookies with jack-o-lantern faces using decorator icing. Top each with 1 gumdrop half for stem.'
// ]

// const notes = [
//   'For Halloween, creme filled chocolate sandwich cookies are available with orange filling; these special festive cookies are perfect for this recipe.'
// ]

export default {
  name: 'Recipe',
  props: {
    id: String,
    msg: String,
    title: String,
    img_link: String,
    time: String,
    serving: String,
    comments: String,
    calories: String,
    ingredients: Array,
    instructions: Array,
    notes: Array
  },
  methods: {
    changeActivekey (key) {
      // console.log('111111')
      console.log(key)
      // var i = 0
      // for (i; i < this.instructions.length; i++) {
      //   if (this.instructions === 'You might also like') {
      //     break
      //   }
      // }
      // this.instructions = this.instructions.slice(0, i)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.ab{
  margin-left: 30%;
  text-align: justify;
  font-size: 17px;
}
</style>
