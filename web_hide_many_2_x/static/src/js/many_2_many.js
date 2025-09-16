/** @odoo-module */
import { Many2ManyTagsField } from "@web/views/fields/many2many_tags/many2many_tags_field";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import {
  useActiveActions
} from "@web/views/fields/relational_utils";

patch(Many2ManyTagsField.prototype, {
  setup() {
    const setup = super.setup();
    this.activeActions = useActiveActions({
      fieldType: "many2many",
      crudOptions: {
        create: false,
        createEdit: false,
        onDelete: false,
        edit: this.props.record.isInEdition,
      },
      getEvalParams: (props) => {
        return {
          evalContext: this.evalContext,
          readonly: props.readonly,
        };
      },
    });

    return setup;
  },
});
