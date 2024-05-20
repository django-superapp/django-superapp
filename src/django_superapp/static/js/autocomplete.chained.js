'use strict';
{
    const $ = django.jQuery;

    $.fn.djangoAdminSelect2Chained = function() {
        $.each(this, function(i, element) {
            const filters = JSON.parse(element.dataset.filters);
            const automaticallySelectUniqueChoice = JSON.parse(element.dataset.automaticallySelectUniqueChoice);
            let lastValues = {};
            for(const key in filters) {
                const relatedFieldElement = $(this).closest('fieldset').find(`[data-field-name=${filters[key]}]`);
                lastValues[filters[key]] = relatedFieldElement.val();
                relatedFieldElement.on('change', () => {
                    if(relatedFieldElement.val() !== lastValues[filters[key]]) {
                        lastValues[filters[key]] = relatedFieldElement.val();

                        if(automaticallySelectUniqueChoice) {
                            const ajaxOptions = $(element).data('select2').options.options.ajax;

                            // Prepare the AJAX request
                            const requestOptions = {
                                url: ajaxOptions.url,
                                dataType: ajaxOptions.dataType,
                                delay: ajaxOptions.delay,
                                data: ajaxOptions.data({ term: "" }), // Add the query term
                                success: function(data) {
                                    if(data['results'].length === 1) {
                                        const firstResult = data['results'][0];
                                        const option = new Option(firstResult.text, firstResult.id, true, true);
                                        $(element).append(option).trigger('change');
                                    } else {
                                        $(element).val(null).trigger('change');
                                    }
                                },
                            };

                            // Perform the AJAX request
                            $.ajax(requestOptions);
                        } else {
                            $(element).val(null).trigger('change');
                        }
                    }
                })
            }

            $(element).select2({
                ajax: {
                    data: (params) => {
                        const filters = JSON.parse(element.dataset.filters);
                        const dynamic_filters = JSON.parse(element.dataset.dynamicFilters);
                        if(dynamic_filters) {
                            for(const key in filters) {
                                const v = $(this).closest('fieldset').find(`[data-field-name=${filters[key]}]`).val();
                                if(v) {
                                    filters[key] = v;
                                }
                            }
                        }

                        return {
                            term: params.term,
                            page: params.page,
                            app_label: element.dataset.appLabel,
                            model_name: element.dataset.modelName,
                            field_name: element.dataset.fieldName,
                            filters: JSON.stringify(filters),
                        };
                    }
                }
            });
        });
        return this;
    };

    $(function() {
        // Initialize all autocomplete widgets except the one in the template
        // form used when a new formset is added.
        $('.admin-autocomplete-chained').not('[name*=__prefix__]').djangoAdminSelect2Chained();
    });

    document.addEventListener('formset:added', (event) => {
        $(event.target).find('.admin-autocomplete-chained').djangoAdminSelect2Chained();
    });
}