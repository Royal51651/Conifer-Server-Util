/// <reference path="../pb_data/types.d.ts" />
migrate((app) => {
  const collection = app.findCollectionByNameOrId("pbc_2605467279")

  // update collection data
  unmarshal({
    "createRule": ""
  }, collection)

  // remove field
  collection.fields.removeById("relation765557111")

  return app.save(collection)
}, (app) => {
  const collection = app.findCollectionByNameOrId("pbc_2605467279")

  // update collection data
  unmarshal({
    "createRule": "User = @request.auth.id"
  }, collection)

  // add field
  collection.fields.addAt(2, new Field({
    "cascadeDelete": false,
    "collectionId": "pbc_949263550",
    "hidden": false,
    "id": "relation765557111",
    "maxSelect": 1,
    "minSelect": 0,
    "name": "User",
    "presentable": false,
    "required": false,
    "system": false,
    "type": "relation"
  }))

  return app.save(collection)
})
