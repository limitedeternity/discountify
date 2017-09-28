(function ($) {

    skel.breakpoints({
        xlarge: '(max-width: 1680px)',
        large: '(max-width: 1280px)',
        medium: '(max-width: 980px)',
        small: '(max-width: 736px)',
        xsmall: '(max-width: 480px)'
    });

    $(function () {

        var $window = $(window),
            $body = $('body'),
            $wrapper = $('#wrapper');

        if (skel.vars.IEVersion < 12)
            $body.addClass('ie');

        if (skel.vars.mobile)
            $body.addClass('touch');

        if (skel.canUse('transition')) {

            $body.addClass('loading');

            $window.on('load', function () {
                window.setTimeout(function () {
                    $body.removeClass('loading');
                }, 100);
            });

            var resizeTimeout;

            $window.on('resize', function () {

                window.clearTimeout(resizeTimeout);

                $body.addClass('resizing');

                resizeTimeout = window.setTimeout(function () {
                    $body.removeClass('resizing');
                }, 100);

            });

        }

        $window.scrollTop(0);

        $('form').placeholder();

        var $panels = $('.panel');

        $panels.each(function () {

            var $this = $(this),
                $toggles = $('[href="#' + $this.attr('id') + '"]'),
                $closer = $('<div class="closer" />').appendTo($this);

            $closer
                .on('click', function (event) {
                    $this.trigger('---hide');
                });

            $this
                .on('click', function (event) {
                    event.stopPropagation();
                })
                .on('---toggle', function () {

                    if ($this.hasClass('active'))
                        $this.triggerHandler('---hide');
                    else
                        $this.triggerHandler('---show');

                })
                .on('---show', function () {

                    if ($body.hasClass('content-active'))
                        $panels.trigger('---hide');

                    $this.addClass('active');
                    $toggles.addClass('active');

                    $body.addClass('content-active');

                })
                .on('---hide', function () {

                    $this.removeClass('active');
                    $toggles.removeClass('active');

                    $body.removeClass('content-active');

                });

            $toggles
                .removeAttr('href')
                .css('cursor', 'pointer')
                .on('click', function (event) {

                    event.preventDefault();
                    event.stopPropagation();

                    $this.trigger('---toggle');

                });

        });

        $body
            .on('click', function (event) {

                if ($body.hasClass('content-active')) {

                    event.preventDefault();
                    event.stopPropagation();

                    $panels.trigger('---hide');

                }

            });

        $window
            .on('keyup', function (event) {

                if (event.keyCode == 27 &&
                    $body.hasClass('content-active')) {

                    event.preventDefault();
                    event.stopPropagation();

                    $panels.trigger('---hide');

                }

            });

        var $header = $('#header');

        $header.find('a').each(function () {

            var $this = $(this),
                href = $this.attr('href');

            if (!href ||
                href.charAt(0) == '#')
                return;

            $this
                .removeAttr('href')
                .css('cursor', 'pointer')
                .on('click', function (event) {

                    event.preventDefault();
                    event.stopPropagation();

                    window.location.href = href;

                });

        });

        var $footer = $('#footer');

        $footer.find('.copyright').each(function () {

            var $this = $(this),
                $parent = $this.parent(),
                $lastParent = $parent.parent().children().last();

            skel
                .on('+medium', function () {
                    $this.appendTo($lastParent);
                })
                .on('-medium', function () {
                    $this.appendTo($parent);
                });

        });

        var $main = $('#main');

        $main.children('.thumb').each(function () {

            var $this = $(this),
                $image = $this.find('.image'),
                $image_img = $image.children('img'),
                x;

            if ($image.length == 0)
                return;


            $image.css('background-image', 'url(' + $image_img.attr('src') + ')');

            if (x = $image_img.data('position'))
                $image.css('background-position', x);

            $image_img.hide();

            if (skel.vars.IEVersion < 11)
                $this
                .css('cursor', 'pointer')
                .on('click', function () {
                    $image.trigger('click');
                });

        });

        $main.poptrox({
            baseZIndex: 20000,
            caption: function ($a) {

                var s = '';

                $a.nextAll().each(function () {
                    s += this.outerHTML;
                });

                return s;

            },
            fadeSpeed: 300,
            onPopupClose: function () {
                $body.removeClass('modal-active');
            },
            onPopupOpen: function () {
                $body.addClass('modal-active');
            },
            overlayOpacity: 0,
            popupCloserText: '',
            popupHeight: 150,
            popupLoaderText: '',
            popupSpeed: 300,
            popupWidth: 150,
            selector: '.thumb > a.image',
            usePopupCaption: true,
            usePopupCloser: true,
            usePopupDefaultStyling: false,
            usePopupForceClose: true,
            usePopupLoader: true,
            usePopupNav: true,
            windowMargin: 50
        });

        skel
            .on('-xsmall', function () {
                $main[0]._poptrox.windowMargin = 50;
            })
            .on('+xsmall', function () {
                $main[0]._poptrox.windowMargin = 0;
            });

    });

})(jQuery);
