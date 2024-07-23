$(document).ready(function() {
    $('#create-rule-form').submit(function(event) {
        event.preventDefault();
        const ruleString = $('#rule').val();

        $.ajax({
            type: 'POST',
            url: '/create_rule',
            contentType: 'application/json',
            data: JSON.stringify({ rule_string: ruleString }),
            success: function(response) {
                alert('Rule created successfully');
                console.log(response.ast);
            },
            error: function(error) {
                alert('Error creating rule');
                console.log(error);
            }
        });
    });

    $('#evaluate-rule-form').submit(function(event) {
        event.preventDefault();
        const ast = $('#ast').val();
        const data = $('#data').val();

        $.ajax({
            type: 'POST',
            url: '/evaluate_rule',
            contentType: 'application/json',
            data: JSON.stringify({ ast: JSON.parse(ast), data: JSON.parse(data) }),
            success: function(response) {
                $('#result').text('Result: ' + response.result);
            },
            error: function(error) {
                alert('Error evaluating rule');
                console.log(error);
            }
        });
    });
});