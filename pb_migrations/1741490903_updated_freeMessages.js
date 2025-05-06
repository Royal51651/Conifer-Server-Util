/// <reference path="../pb_data/types.d.ts" />
migrate((app) => {
  const collection = app.findCollectionByNameOrId("pbc_721422533")

  // remove field
  collection.fields.removeById("text19424289")

  return app.save(collection)
}, (app) => {
  const collection = app.findCollectionByNameOrId("pbc_721422533")

  // add field
  collection.fields.addAt(2, new Field({
    "autogeneratePattern": "",
    "hidden": false,
    "id": "text19424289",
    "max": 0,
    "min": 0,
    "name": "Username",
    "pattern": "",
    "presentable": false,
    "primaryKey": false,
    "required": false,
    "system": false,
    "type": "text"
  }))

  return app.save(collection)
})
