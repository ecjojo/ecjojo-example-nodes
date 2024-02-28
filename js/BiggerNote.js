import { app } from "/scripts/app.js";
import { ComfyWidgets } from "/scripts/widgets.js";

app.registerExtension({
  name: "Comfy.BiggerNote",

  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (nodeData.name === "BiggerNote_Example") {
      nodeType.prototype.onNodeCreated = function () {
        const nodeName = `${nodeData.name}`;

        // const intWidget = ComfyWidgets.INT(
        //   this,
        //   "FontSize",
        //   ["INT",  {default: 24} ],
        //   app
        // );

        const textWidget = ComfyWidgets.STRING(
          this,
          nodeName,
          ["STRING", { default: "", placeholder: "Enter text here...", multiline: true }],
          app
        );

        textWidget.widget.inputEl.style.fontSize = "24px";
        
        //intWidget.widget.inputEl.addEventListener('change', (e) => {
         //  const newFontSize = intWidget.widget.inputEl.value + "px";
          // textWidget.widget.inputEl.style.fontSize = newFontSize;
        //});

      return { textWidget, intWidget };
      };
    }
  },
});