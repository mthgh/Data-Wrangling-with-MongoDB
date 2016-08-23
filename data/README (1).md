



<!DOCTYPE html>
<html lang="en" class=" is-copy-enabled is-u2f-enabled">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-11a662d59757ef2ced3c65b6a175b2ebad3770c188a3b2cc0025b735fc78867c.css" integrity="sha256-EaZi1ZdX7yztPGW2oXWy6603cMGIo7LMACW3Nfx4hnw=" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-61cb2093569500898220e7ec87febebd8950aa1361eb9e29cec388050a0fa544.css" integrity="sha256-Ycsgk1aVAImCIOfsh/6+vYlQqhNh654pzsOIBQoPpUQ=" media="all" rel="stylesheet" />
    
    
    
    

    <link as="script" href="https://assets-cdn.github.com/assets/frameworks-74e2880351ce368d8f0a52f12a7452b422bef6397d5477d8120207ea79f0dfd9.js" rel="preload" />
    
    <link as="script" href="https://assets-cdn.github.com/assets/github-571ebb984301f1ae281586ba34ea23b25bb49241cb765a7e4c6e855b42ed5b55.js" rel="preload" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=device-width">
    
    <title>Data-Wrangling-with-MongoDB/README.md at master · mthgh/Data-Wrangling-with-MongoDB</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="https://avatars0.githubusercontent.com/u/20431956?v=3&amp;s=400" name="twitter:image:src" /><meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="mthgh/Data-Wrangling-with-MongoDB" name="twitter:title" /><meta content="Contribute to Data-Wrangling-with-MongoDB development by creating an account on GitHub." name="twitter:description" />
      <meta content="https://avatars0.githubusercontent.com/u/20431956?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="mthgh/Data-Wrangling-with-MongoDB" property="og:title" /><meta content="https://github.com/mthgh/Data-Wrangling-with-MongoDB" property="og:url" /><meta content="Contribute to Data-Wrangling-with-MongoDB development by creating an account on GitHub." property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MjA0MzE5NTY6N2QxNjQ1NjZjOWQ1NzExM2Q0ZWUyNjFjMzIyOWI1ZDE6NGY5ODhlMWMzZjVhY2ZiYmJiMzc0MzVjM2FiYmVjNzFiNWRkYTY2NTI3NjdjOTQyMzg5MGZiNWI5NTgxNWEyYQ==--d2f86757b09ca01110e92725a07d19c07baacca3">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">
    <meta name="request-id" content="82D77D45:2CFCD:53F4C2F:57BC79EE" data-pjax-transient>

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="82D77D45:2CFCD:53F4C2F:57BC79EE" name="octolytics-dimension-request_id" /><meta content="20431956" name="octolytics-actor-id" /><meta content="mthgh" name="octolytics-actor-login" /><meta content="29aafe7a40684c1424ca9905e71b05e9dcd2bfed61cda8a7b624cb499260db28" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />



  <meta class="js-ga-set" name="dimension1" content="Logged In">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="mthgh">

        <meta name="expected-hostname" content="github.com">
      <meta name="js-proxy-site-detection-payload" content="MmUwY2U5YmJhNTQyNDcyY2NhOTU2YWM5ODhlNzg2Mjk2NDM1Yjk0OTA4NmE5ZWE1ZjgzODk4ODVhZmExMmMwOXx7InJlbW90ZV9hZGRyZXNzIjoiMTMwLjIxNS4xMjUuNjkiLCJyZXF1ZXN0X2lkIjoiODJENzdENDU6MkNGQ0Q6NTNGNEMyRjo1N0JDNzlFRSIsInRpbWVzdGFtcCI6MTQ3MTk2OTc4M30=">


      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta name="html-safe-nonce" content="5d80eca7914529c4410c2a76fd70f83f786f6fde">
    <meta content="0f41c97369ed524f8909193f23cd7b3502b10eb7" name="form-nonce" />

    <meta http-equiv="x-pjax-version" content="588274188c1c987c1b59b13a46673913">
    

      
  <meta name="description" content="Contribute to Data-Wrangling-with-MongoDB development by creating an account on GitHub.">
  <meta name="go-import" content="github.com/mthgh/Data-Wrangling-with-MongoDB git https://github.com/mthgh/Data-Wrangling-with-MongoDB.git">

  <meta content="20431956" name="octolytics-dimension-user_id" /><meta content="mthgh" name="octolytics-dimension-user_login" /><meta content="65954402" name="octolytics-dimension-repository_id" /><meta content="mthgh/Data-Wrangling-with-MongoDB" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="65954402" name="octolytics-dimension-repository_network_root_id" /><meta content="mthgh/Data-Wrangling-with-MongoDB" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/mthgh/Data-Wrangling-with-MongoDB/commits/master.atom" rel="alternate" title="Recent Commits to Data-Wrangling-with-MongoDB:master" type="application/atom+xml">


      <link rel="canonical" href="https://github.com/mthgh/Data-Wrangling-with-MongoDB/blob/master/README.md" data-pjax-transient>
  </head>


  <body class="logged-in  env-production windows vis-public page-blob">
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="28" version="1.1" viewBox="0 0 16 16" width="28"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>


        <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/mthgh/Data-Wrangling-with-MongoDB/search" class="js-site-search-form" data-scoped-search-url="/mthgh/Data-Wrangling-with-MongoDB/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
    </label>
</form></div>


      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
    

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <svg aria-hidden="true" class="octicon octicon-plus left" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"></path></svg>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>


  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="mthgh/Data-Wrangling-with-MongoDB">This repository</span>
  </div>
    <a class="dropdown-item" href="/mthgh/Data-Wrangling-with-MongoDB/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>
    <a class="dropdown-item" href="/mthgh/Data-Wrangling-with-MongoDB/settings/collaboration" data-ga-click="Header, create new collaborator">
      New collaborator
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/mthgh"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@mthgh" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/20431956?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu dropdown-menu-sw">
        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">mthgh</strong>
        </div>

        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/mthgh" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a>
          <a class="dropdown-item" href="/stars" data-ga-click="Header, go to starred repos, text:your stars">
            Your stars
          </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
          <a class="dropdown-item" href="/integrations" data-ga-click="Header, go to integrations, text:integrations">
            Integrations
          </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>


        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a>

        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="0f41c97369ed524f8909193f23cd7b3502b10eb7" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="uPIsxitVTLwi3h+ApSOGB80QDbmFG4UeQ5xbPXDd+BIlMyrfTqner2kOnR9dF6pXJjpXNHmAlU/pPYEWF0nnZA==" /></div>
          <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>


      


    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="0f41c97369ed524f8909193f23cd7b3502b10eb7" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="LF/CFYR0QYuMP2dXVCOouRoUEC+fk2Sa8HbPbBxgejLImtpbCelXase6gup/zXBnMzh7koyHQqKH8Ry/JYS0uQ==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="65954402" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/mthgh/Data-Wrangling-with-MongoDB/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
              <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
              Unwatch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/mthgh/Data-Wrangling-with-MongoDB/watchers"
            aria-label="1 user is watching this repository">
            1
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                      Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"></path></svg>
                      Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/mthgh/Data-Wrangling-with-MongoDB/unstar" class="starred" data-form-nonce="0f41c97369ed524f8909193f23cd7b3502b10eb7" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Aliz2viM6xExuy0XAGh9FiUuYtlGLJJPGkdsEZzGXvV1CDXx3amHuc8sXMRQFLSeu4tYYW0UJdHw3RXkLpPYNA==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar mthgh/Data-Wrangling-with-MongoDB"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/mthgh/Data-Wrangling-with-MongoDB/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/mthgh/Data-Wrangling-with-MongoDB/star" class="unstarred" data-form-nonce="0f41c97369ed524f8909193f23cd7b3502b10eb7" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="9ifN9YktTsjkXODEl40s3KqQAtW24M9JORoCUiwC3ISRYvmqsPIcF/DvPNILQqN3mB7mLsiakiPePibxcvg/Ig==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star mthgh/Data-Wrangling-with-MongoDB"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"></path></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/mthgh/Data-Wrangling-with-MongoDB/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/mthgh/Data-Wrangling-with-MongoDB/fork" class="btn-with-count" data-form-nonce="0f41c97369ed524f8909193f23cd7b3502b10eb7" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="uUnEJmQhYOls2bwt6QyW3X0ZhudMumZ/6L+8Nuj5PYdFRiP7LYlPNCqaIrVbjodO1uzsYQur+bFZtEmcYPYYTQ==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of mthgh/Data-Wrangling-with-MongoDB to your account"
                aria-label="Fork your own copy of mthgh/Data-Wrangling-with-MongoDB to your account">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
              Fork
            </button>
</form>
    <a href="/mthgh/Data-Wrangling-with-MongoDB/network" class="social-count"
       aria-label="0 users are forked this repository">
      0
    </a>
  </li>
</ul>

    <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
  <span class="author" itemprop="author"><a href="/mthgh" class="url fn" rel="author">mthgh</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/mthgh/Data-Wrangling-with-MongoDB" data-pjax="#js-repo-pjax-container">Data-Wrangling-with-MongoDB</a></strong>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/mthgh/Data-Wrangling-with-MongoDB" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /mthgh/Data-Wrangling-with-MongoDB" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/mthgh/Data-Wrangling-with-MongoDB/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /mthgh/Data-Wrangling-with-MongoDB/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/mthgh/Data-Wrangling-with-MongoDB/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /mthgh/Data-Wrangling-with-MongoDB/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a href="/mthgh/Data-Wrangling-with-MongoDB/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /mthgh/Data-Wrangling-with-MongoDB/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"></path></svg>
      Wiki
</a>

  <a href="/mthgh/Data-Wrangling-with-MongoDB/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /mthgh/Data-Wrangling-with-MongoDB/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"></path></svg>
    Pulse
</a>
  <a href="/mthgh/Data-Wrangling-with-MongoDB/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /mthgh/Data-Wrangling-with-MongoDB/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"></path></svg>
    Graphs
</a>
    <a href="/mthgh/Data-Wrangling-with-MongoDB/settings" class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations /mthgh/Data-Wrangling-with-MongoDB/settings">
      <svg aria-hidden="true" class="octicon octicon-gear" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88-1.84-1.13-1.13-1.81.91-1.09-.45-.69-1.92h-1.6l-.63 1.94-1.11.45-1.84-.88-1.13 1.13.91 1.81-.45 1.09L0 7.23v1.59l1.94.64.45 1.09-.88 1.84 1.13 1.13 1.81-.91 1.09.45.69 1.92h1.59l.63-1.94 1.11-.45 1.84.88 1.13-1.13-.92-1.81.47-1.09L14 8.75v.02zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"></path></svg>
      Settings
</a>
</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/mthgh/Data-Wrangling-with-MongoDB/blob/33c89c45669d69fb509df5960883c31b44cb5123/README.md" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:85480a1f8db4e717e33b18ae67ad7d03 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/mthgh/Data-Wrangling-with-MongoDB/blob/master/README.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/mthgh/Data-Wrangling-with-MongoDB/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" data-form-nonce="0f41c97369ed524f8909193f23cd7b3502b10eb7" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="8N16WK//mN3rfLnNA9thkjeSjAQsPAfaMqq7HnqcBemGV8Df9lgEkw61tNTwj0k9i27zWSPgVxNyeo0y1gg/VA==" /></div>
          <svg aria-hidden="true" class="octicon octicon-git-branch select-menu-item-icon" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M10 5c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v.3c-.02.52-.23.98-.63 1.38-.4.4-.86.61-1.38.63-.83.02-1.48.16-2 .45V4.72a1.993 1.993 0 0 0-1-3.72C.88 1 0 1.89 0 3a2 2 0 0 0 1 1.72v6.56c-.59.35-1 .99-1 1.72 0 1.11.89 2 2 2 1.11 0 2-.89 2-2 0-.53-.2-1-.53-1.36.09-.06.48-.41.59-.47.25-.11.56-.17.94-.17 1.05-.05 1.95-.45 2.75-1.25S8.95 7.77 9 6.73h-.02C9.59 6.37 10 5.73 10 5zM2 1.8c.66 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2C1.35 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2zm0 12.41c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm6-8c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="README.md">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/mthgh/Data-Wrangling-with-MongoDB/find/master"
          class="js-pjax-capture-input btn btn-sm"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/mthgh/Data-Wrangling-with-MongoDB"><span>Data-Wrangling-with-MongoDB</span></a></span></span><span class="separator">/</span><strong class="final-path">README.md</strong>
  </div>
</div>


  <div class="commit-tease">
      <span class="right">
        <a class="commit-tease-sha" href="/mthgh/Data-Wrangling-with-MongoDB/commit/dbc26b4d1361a81e82840fa013428b1fac6780fe" data-pjax>
          dbc26b4
        </a>
        <relative-time datetime="2016-08-23T03:33:31Z">Aug 22, 2016</relative-time>
      </span>
      <div>
        <img alt="@mthgh" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/20431956?v=3&amp;s=40" width="20" />
        <a href="/mthgh" class="user-mention" rel="author">mthgh</a>
          <a href="/mthgh/Data-Wrangling-with-MongoDB/commit/dbc26b4d1361a81e82840fa013428b1fac6780fe" class="message" data-pjax="true" title="Update README.md">Update README.md</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>1</strong>
         contributor
      </button>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@mthgh" height="24" src="https://avatars2.githubusercontent.com/u/20431956?v=3&amp;s=48" width="24" />
            <a href="/mthgh">mthgh</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="btn-group">
      <a href="/mthgh/Data-Wrangling-with-MongoDB/raw/master/README.md" class="btn btn-sm " id="raw-url">Raw</a>
        <a href="/mthgh/Data-Wrangling-with-MongoDB/blame/master/README.md" class="btn btn-sm js-update-url-with-hash">Blame</a>
      <a href="/mthgh/Data-Wrangling-with-MongoDB/commits/master/README.md" class="btn btn-sm " rel="nofollow">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://windows.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg aria-hidden="true" class="octicon octicon-device-desktop" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"></path></svg>
        </a>

        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/mthgh/Data-Wrangling-with-MongoDB/edit/master/README.md" class="inline-form js-update-url-with-hash" data-form-nonce="0f41c97369ed524f8909193f23cd7b3502b10eb7" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ZrbF27PcNU9YKPbA+cGwuIvpb/MzNM7KjKQoXFrHaay56iBvsFl/XSmkJGkIs5ALVMjYOCna7yZz/VK4+Z9iWw==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Edit this file" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg>
          </button>
</form>        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/mthgh/Data-Wrangling-with-MongoDB/delete/master/README.md" class="inline-form" data-form-nonce="0f41c97369ed524f8909193f23cd7b3502b10eb7" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="d9+n9J8DYh2h13QS4x1Jdfrr3vPJZsk+3CDlIBo5IdbRPNLEE1CYKkbPSGo7EcAaCYmSo98GZprpBK7tlOnx9w==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete this file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"></path></svg>
          </button>
</form>  </div>

  <div class="file-info">
      248 lines (213 sloc)
      <span class="file-info-divider"></span>
    20.6 KB
  </div>
</div>

  
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a id="user-content-fianl-project-for-data-wrangling-with-mongodb" class="anchor" href="#fianl-project-for-data-wrangling-with-mongodb" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Fianl Project for Data Wrangling with MongoDB</h1>

<h2><a id="user-content-contents" class="anchor" href="#contents" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Contents</h2>

<ol>
<li><a href="#summary">Project Summary</a></li>
<li><a href="#clean">Data Cleaning</a>

<ol>
<li><a href="#count">overview of the dataset</a></li>
<li><a href="#fix_tagkey">problematic tag keys</a></li>
<li><a href="#putDB">put to mongodb</a></li>
<li><a href="#fix_state">problematic addr:state</a></li>
<li><a href="#fix_city">problematic addr:city</a></li>
<li><a href="#fix_street">problematic addr:street</a></li>
<li><a href="#fix_postcode">problematic addr:postcode</a></li>
<li><a href="#fix_housenumber">problematic addr:housenumber</a></li>
<li><a href="#fix_amenity">problematic amenity</a></li>
<li><a href="#json">output to json</a></li>
</ol></li>
<li><a href="#overview">Data Overview</a></li>
<li><a href="#addtional">Additional Ideas</a></li>
</ol>

<h2><a id="user-content-1-project-summary" class="anchor" href="#1-project-summary" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-summary"></a>1. Project Summary</h2>

<p>This is the final project from udacity's online course "Data Wrangling with MongoDB". The task is to choose any area of the world from <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a> and use data munging techniques, such as assessing the quality of the data for validity, accuracy, completeness, consistency and uniformity, to clean the OpenStreetMap data.</p>

<p><strong><em>Map Area : Great New York City Area</em></strong><br>
<strong><em>Open Street Map URL</em></strong>: <a href="https://www.openstreetmap.org/export#map=10/40.7202/-73.8638">https://www.openstreetmap.org/export#map=10/40.7202/-73.8638</a><br>
<strong><em>Data Source (OSM XML)</em></strong>: <a href="https://mapzen.com/data/metro-extracts/metro/new-york_new-york/">https://mapzen.com/data/metro-extracts/metro/new-york_new-york/</a></p>

<p><strong><em>File Sizes</em></strong>:<br>
ny.osm: 2.13GB  (original OSM XML file)<br>
ny.json: 2.73GB (after converting original OSM XML file to json file)</p>

<p><strong><em>References</em></strong>:  </p>

<ul>
<li>OSM tag keys: <a href="http://wiki.openstreetmap.org/wiki/Map_Features">http://wiki.openstreetmap.org/wiki/Map_Features</a></li>
<li>US town names (US.zip): <a href="http://download.geonames.org/export/dump/">http://download.geonames.org/export/dump/</a></li>
<li>Prefix of postcodes: <a href="https://en.wikipedia.org/wiki/List_of_ZIP_code_prefixes">https://en.wikipedia.org/wiki/List_of_ZIP_code_prefixes</a></li>
</ul>

<h2><a id="user-content-2-data-cleaning" class="anchor" href="#2-data-cleaning" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-clean"></a>2. Data Cleaning</h2>

<h3><a id="user-content-i-overview-of-the-dataset" class="anchor" href="#i-overview-of-the-dataset" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-count">i. overview of the dataset</a></h3><a name="user-content-count">

<p>To get an idea of the size of the dataset, <code>elem_count.py</code> was used to count the element, attribute and tagkeys present in this dataset. With the result showing below. (Only node, way and the corresponding subelements will be processed later on to mongodb)</p>

<pre> Element Count:          Attrib Count:                          Total Number of Distinct Tagkeys: 1469
 {'bounds': 1,           {'node_changeset': 9125861,            
 'member': 98515,         'node_id': 9125861,                   Tagkey Types Count:
 'nd': 11821306,          'node_lat': 9125861,                  {'UpperNums_colon': 70370,
 'node': 9125861,         'node_lon': 9125861,                   'dots': 24991,
 'osm': 1,                'node_timestamp': 9125861,             'lower': 3392866,
 'relation': 8081,        'node_uid': 9125861,                   'others': 27,
 'tag': 8630865,          'node_user': 9125861,                  'problemchars': 7,
 'way': 1503605}          'node_version': 9125861,               'single_colon': 5109466,
                          'tag_k': 8630865,                      'UpperNums': 33138,}
                          'tag_v': 8630865,                    
                          'way_changeset': 1503605,            Tagkeys Count(stored in data/tagkeys_stats.txt):
                          'way_id': 1503605,                   {'building': 1197472,
                          'way_timestamp': 1503605,             'height': 1102643,
                          'way_uid': 1503605,                   'nycdoitt:bin': 1079114,
                          'way_user': 1503605,                  'addr:street': 927273,
                          'way_version': 1503605}               ......}
</pre>

</a><h3><a id="user-content-ii-problematic-tag-keys" class="anchor" href="#ii-problematic-tag-keys" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-count"></a><a name="user-content-fix_tagkey">ii. problematic tag keys</a></h3><a name="user-content-fix_tagkey">

<p>From the result above in point i, every tag key was counted. It was found that many of tag keys appear only once. In order to pick up resonable tag keys for processing, functions in <code>fix_tagkeys.py</code> were used to fix tagkeys.  </p>

<p>First, a distribition of the count of the tag keys were calculated (stored in "distrib" variable)  </p>

<pre><code>'total num of distinct keys = 1469',  
'total num of keys = 8630865',  
'num of keys count more than 86308 times (0.01*total_count) = 16',  
'num of keys count more than 8630 times (0.001*total_count) = 51',  
'num of keys count more than 863 times (0.0001*total_count) = 148',  
'num of keys count more than 86 times (0.00001*total_count) = 322',  
'num of keys count more than 8 times (0.000001*total_count) = 593'  
</code></pre>

<p>Based on the result, only keys appear more than 0.00001*total_count times (86 times) will be processed (stored inside variable "keys_v1"). The other keys are so rare, or they might have the meaning with one of the keys appear more often. For example, "alt_name_1" which appear 4 times most likely to have the same meaning as "alt_name" (appear 1442 times). Also, something like "to" (appear 57 times) is ambiguous and something like "name:wa" (appear 1 time) is so rare.  </p>

</a><p><a name="user-content-fix_tagkey">Second, for the 322 tag keys that appear more than 86 times (stored inside variable "keys_v1"), they are compared with common standard keys from  </a><a href="http://wiki.openstreetmap.org/wiki/Map_Features">http://wiki.openstreetmap.org/wiki/Map_Features</a> (the standard keys on this web page were crawled using "BeautifulSoup" lib and stored inside "official_keySet" variable). Of the 322 tag keys, 102 of them exists as standard keys and will be processed without change, the other 220 keys (stored inside "key_need_check" variable) will need further fix.</p>

<p>Third, for the other 220 keys need to check, their types were investigated (if they contain colon, if they contain specific characters, etc), the result was stored in "prob_key_types" variable. Based on the findings, for keys only contain lower case characters, if they appear more than 0.0001*total_count times (863 times), they are saved. For keys contain colon, they are saved if the first part before the colon was a standard key (except the meaning of the second part is ambigous), or if the first part appear more than 0.0001*total_count times (863 times) on average. Some of the keys are problematic, like "cityracks.housenum", in this case, the dot was changed to colon to keep consistency. of the 220 keys, the saved keys were stored in "fixed_key" variable. (The combined fix from this paragraph and last paragraph were stored in "keys_v2" variable)</p>

<p>Fourth, it was found that something like "building" and "building:levels" both exist. Such keys exist both as itself and as the first part in a colon-containing key. This will bring trouble to process into a dictionary because of the key confilict (cannot have dict[building] = value and dict[building] = {"levels":value} both exist). Therefore, for such keys, they are changed to "keys:keys" format (for example, "building" changed to "building:building")</p>

<p>After all the four steps fix, the final keys and the counts were stored in "final_keys" variable. old key to new key mapping was stored in "key_map" variable, it could also be found in data/key_map.txt. </p>

<h3><a id="user-content-iii-put-to-mongodb" class="anchor" href="#iii-put-to-mongodb" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-putDB">iii. put to mongodb</a></h3><a name="user-content-putDB">

<p>After initial fixation of the tag keys, before further cleaning on other fields, the dataset was loaded into mongodb (Only Node, Way and respective sub-elements were loaded into database) using <code>put_to_db.py</code>. The following structure was used to import the dataset.</p>

<pre>Node Elem:                                                Way Elem:
{u'types': u'node',                                       {u'types': u'way',
 u'created': {u'changeset': unicode,                       u'created': {u'changeset': unicode,      
              u'timestamp': datetime.datetime,                          u'timestamp': datetime.datetime,
              u'uid': unicode,                                          u'uid': unicode,
              u'user': unicode,                                         u'user': unicode,
              u'version': unicode},                                     u'version': unicode},
 u'id': unicode,                                           u'id': unicode,
 u'pos': [float(lon), float(lat)] }                        u'nd': [unicode, unicode]}
</pre>
 

<p>"tag" were added to the corresponding "node" and "way" element with the attribute k/v as key/value pairs :</p>

<pre>tag keys do not have colon: Element[k] = v
tag keys having one colon: Element[k_first_section] = {k_second_section:v}
tag keys having two colon: Element[k_first_section] = {k_second_section:{third_section:v}}
 
example:
                                                                            {...
&lt;tag k="addr:street:name" v="Lincoln"/&gt;       should be turned into:        "addr": {
&lt;tag k="amenity" v="pharmacy"/&gt;                                                      "housenumber": 5158,
&lt;tag k="addr:housenumber" v="5158"/&gt;                                                 "street": {"name":"Lincoln"},
                                                                                    }
                                                                            "amenity": "pharmacy",
                                                                            ...}
</pre>

</a><h3><a id="user-content-iv-problematic-addrstate" class="anchor" href="#iv-problematic-addrstate" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-putDB"></a><a name="user-content-fix_state">iv. problematic addr:state</a></h3><a name="user-content-fix_state">

<p><code>fix_state.py</code> was used to audit the "addr:state" field and fix the state values. Using <code>fix_state.py</code>, distinct values of "addr.state" in the database were obtained (stored in "dist_state" variable). It was found that the state names exist in several different forms, like "New York", "NJ - New Jersey", "ct", etc. To make the values consistent, these forms were all converted to the abbrevation of the corresponding state with upper letters, ie, "NY", "NJ" and "CT". </p>

<p>Also, unexpected state names like "ON", "BY", "TX", "CA", "10009" and so on were found. The corresponding instances were extracted from the database and turns out that the state names were all mistake inputs caused by user. Therefore, they were updated to the right names ("NY", "NJ", or "CT"). </p>

<p>The mapping of the old state name to new state name was stored in "state_map" variable.</p>

</a><h3><a id="user-content-v-problematic-addrcity" class="anchor" href="#v-problematic-addrcity" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-fix_state"></a><a name="user-content-fix_city">v. problematic addr:city</a></h3><a name="user-content-fix_city">

<p><code>fix_city.py</code> was used to audit the "addr:city" field and fix the city values. Upon getting the distinct city names (stored in "dist_city"), it was found that some of the city names contain state or postcode infomations. like "Merrick, New York", 'New Brunswick, NJ 08901', 'Fresh Meadows NY' and so on. In order to fix them, these values were updated to the correct city names, and the state or postcode info were also moved the right field("addr:state" and "addr:postcode").  </p>

</a><p><a name="user-content-fix_city">The city names were also compared to the standard town database (could be found in folder "data/US_town.txt". This txt file was downloaded from </a><a href="http://download.geonames.org/export/dump/">http://download.geonames.org/export/dump/</a> as tab-delimited text, a discription of the database could be found on the website as well), the standard town names were processed into a variable "ny_town" as a list. 45 of the 412 city names could not be found from "ny_town". some of them are due to typos, like "Brookklyn" (should be "Brooklyn"), some are not in the right format, like "Hasbrouck Hts" (should be "Hasbrouck Heights"), some are valid names but not in "ny_town" that was processed, like "Bronx" (in this work, the value for the "feature class" field processed is "P", but "Bronx" is in "A" catagory, see description of the database for detail), others are ambigous, like "M", "2", etc.The problematic city names were either updated, kept unchanged, or deleted. Final mapping of original city name to the updated city name could be found in variable "city_map"</p>

<h3><a id="user-content-vi-problematic-addrstreet" class="anchor" href="#vi-problematic-addrstreet" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-fix_street">vi. problematic addr:street</a></h3><a name="user-content-fix_street">

<p><code>fix_street.py</code> was used to audit the "addr:street" field and fix the street values.There are 9452 distinct street in this dataset. (stored in "dist_street" variable). </p>

<p>First, street names were converted to a uniform format using "street_name.strip().title()".  </p>

<p>Second, it was found that some street names contain unusual characters, like "#", ",", "\" and so on. Some of the characters were used to indicate alternative names, like "US 1 (Brunswick Pike)"; Some of them were used for housenumbers, like 'H Highway 34 #120'; Some are ambigous, like '37th Avenue, 14th Street, 21st Street'; Some of them were valid, but different formats exists, like "George's Road" and "Georges Road", they are the same road but with different formats. In order to fix, all special characters were removed to keep unification ("George's Road" convert to "Georges Road", "U.S. 1" convert to "Us 1", 'NJ-36' convert to "Nj 36", '102 St.' convert to "102 St", etc). Redundant info (like alternative names, housenumbers, etc) were removed. And if the street names were ambigous, they were deleted.  </p>

<p>Third, it was found that in some cases, the street name suffixs were abbreviated (like "10th Ave"); in other cases, full suffixs were used (like '10th Avenue'); To fix the problem: for the formal case where the suffixs were abbreviated, they were converted to the full suffixs ('Harbor Dr' to "Harbor Drive", "10th Ave" to "10Th Avenue", etc).  </p>

<p>Fourth, for the street names do not end with an "expected suffixs" ("Parkway", "Drive", "Expressway", etc), there are several cases:<br>
      In one case, the street names contain the "expected suffix" in the middle instead of at the end and redundant info exist (like 'West 80th Street NYC 10024'). To fix, the redundant info were removed ('West 80th Street NYC 10024' to "West 80Th Street");<br>
      In second case, the street names were valid and they are highways, like 'NJ 35', 'NJ Route 35', 'South New Jersey 17Th South', 'State Route 36', 'US 1', 'US Highway 1 North', 'US Highway 1', etc. There are multiple formats of the highways. To make the format consistent, direction info were removed (remove "North", "South", etc), and only "State Route", "Route" and "Us" were used before the numbers (the above sample highway names were converted to 'State Route 35', 'State Route 35', "State Route 17", 'State Route 36', 'Us 1', 'Us 1' and 'Us 1' respectively. See "street_map" and code for detail);<br>
      In third case, street names are valid, like "Avenue Of Puerto Rico", they are saved without change;<br>
      In fourth case, street names are not valid and they are deleted, like "Washington Square Village", 'ROAD 1', etc.</p>

<p>Fifty, some street names contain housenumber info at the front, like "40 W 94Th Street", '505Th 8Th Avenue'. In this case, the housenumber info were removed ("40 W 94Th Street" to "W 94Th Street"; '505Th 8Th Avenue' to "8Th Avenue").</p>

<p>Sixth, some street names do not have the right number format, like '7 Avenue', '102 Street', 'Third Avenue', 'Fifth Avenue', etc. They were converted to '7Th Avenue', '102Th Street', '3Rd Avenue' and '5Th Avenue' respectively.</p>

<p>Seventh, it was found that some street names start with directions ("East", "West", etc). For street names starting with directions, some of them have full direction, like 'East 73rd Street', some of them have abbreviated directions, like 'E 73rd Street'. To fix, the abbreviated directions were converted to full word ('E 73rd Street' to "East 73Rd Street").</p>

<p>The mapping of the original street names to the updated street names were stored in variable "street_map"</p>

</a><h3><a id="user-content-vii-problematic-addrpostcode" class="anchor" href="#vii-problematic-addrpostcode" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-fix_street"></a><a name="user-content-fix_postcode">vii. problematic addr:postcode</a></h3><a name="user-content-fix_postcode">

<p><code>fix_postcode.py</code> was used to audit the "addr:postcode" field and fix the postcode values.</p>

<p>It was expected that postcode should be five digit numbers. However, it was found that nine digit postcode exist ('11201-2483'), and postcode with state info exist ('NY 10533'). To fix, the nine digit postcodes were convert to five digit postcodes ('11201-2483' to '11201') and for postcodes with state info, the state info was deleted ('NY 10533' to '10533'). </p>

</a><p><a name="user-content-fix_postcode">Other unexpected postcodes including something like '100014' (should be "10014"), which is due to typos; 'New York, NY 10065' (should be "10065") which contain redundant info; '40299', which is not a valid postcode in NJ, NY or CT (</a><a href="https://en.wikipedia.org/wiki/List_of_ZIP_code_prefixes">https://en.wikipedia.org/wiki/List_of_ZIP_code_prefixes</a>); "(718) 778-0140", which is abviously a phone number instead of postcode. Such problematic postcodes were all corrected (in the case of invalid postcode like "40299", they are deleted).</p>

<p>The mapping of old postcodes to new postcodes were stored in "postcode_map" variable.</p>

<h3><a id="user-content-viii-problematic-addrhousenumber" class="anchor" href="#viii-problematic-addrhousenumber" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-fix_housenumber">viii. problematic addr:housenumber</a></h3><a name="user-content-fix_housenumber">

<p><code>fix_housenumber.py</code> was used to audit the "addr:housenumber" field and fix the housenumber values.</p>

<p>First, it was found that in some cases, the "addr.housenumber" field has a value, but the "addr.street" field does not have values. Such housenumbers exist without any street names. They were considered invalid and were deleted (except in cases where the housenumber include street names, like '359 van Brunt'. In such cases, the correct housenumber ("359") were extracted and the street names ('Van Brunt') were put to "addr.street" field, mapping is stored in variable "housenumber_map_1").</p>

<p>Second, it was found that in the field of "addr.housenumber", values like '502 9th Avenue', '30 Vesey St' and so on exists. Such values were a mix of housenumber and street names. To fix such values, housenumbers were kept and street names were deleted. The mapping is stored in variable "housenumber_map_2".</p>

</a><h3><a id="user-content-ix-problematic-amenity" class="anchor" href="#ix-problematic-amenity" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-fix_housenumber"></a><a name="user-content-fix_amenity">ix. problematic amenity</a></h3><a name="user-content-fix_amenity">

<p><code>fix_amenity.py</code> was used to audit the "amenity" field and fix the amenity values.</p>

<p>153 distinct amenity values exist (stored in "dist_amenity" variable). After checking all the values, several problems were found: First, some values have the same meaning, like 'waste_disposal' and "waste_basket" both exist and they have the same meaning. To fix, 'waste_disposal' was converted to "waste_basket", since the latter one appear more times. Second, some values were misunderstanding, like 'user_defined', 'school;place_of_worship', etc. they were either deleted (formal case), or updated (latter case,'school;place_of_worship' convert to 'school' according to detailed descriptions in this piece of data). Third, some of the values do not have the right format or contain typos, like "Liquor_Store", 'Family health clinic', 'pakring', etc. They were converted to the right format ("liquor_store", 'family_health_clinic' and 'parking' respectively).The mapping of the change was stored in "amenity_map" variable.</p>

</a><h3><a id="user-content-x-output-to-json" class="anchor" href="#x-output-to-json" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-fix_amenity"></a><a name="user-content-json">x. output to json</a></h3><a name="user-content-json">

<p>cmd command <code>mongoexport -d osm -c NY_osm -o ny.json</code> was used to export the mongodb dataset to json file.</p>

</a><h2><a id="user-content-3-data-overview" class="anchor" href="#3-data-overview" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a name="user-content-json"></a><a name="user-content-overview"></a>3. Data Overview</h2>

<p>Number of documents</p>

<pre>&gt; db.NY_osm.find().count()
10629466
</pre>

<p>Number of nodes</p>

<pre>&gt; db.NY_osm.find({"types":"node"}).count()
9125861
</pre>

<p>Number of ways</p>

<pre>&gt; db.NY_osm.find({"types":"way"}).count()
1503605
</pre>

<p>Number of unique users</p>

<pre>&gt; db.NY_osm.distinct("created.user").length
3591
</pre>

<p>Top 5 contributing user</p>

<pre>&gt; db.NY_osm.aggregate([{"$group":{"_id":"$created.user",
                                 "count":{"$sum":1}}},
                      {"$sort":{"count":-1}},
                      {"$limit":5}])
{ "_id" : "Rub21_nycbuildings", "count" : 4891073 }
{ "_id" : "ingalls_nycbuildings", "count" : 935873 }
{ "_id" : "woodpeck_fixbot", "count" : 640476 }
{ "_id" : "ediyes_nycbuildings", "count" : 272014 }
{ "_id" : "lxbarth_nycbuildings", "count" : 234580 }
</pre>

<p>Number of users contributing only once</p>

<pre>&gt; db.NY_osm.aggregate([{"$group":{"_id":"$created.user",
                                 "count":{"$sum":1}}},
                      {"$group":{"_id":"$count",
                                 "num_users":{"$sum":1}}},
                      {"$sort":{"_id":1}},
                      {"$limit":1}])
{ "_id" : 1, "num_users" : 920 }
</pre>

<p>Top 5 amenities:</p>

<pre>&gt; db.NY_osm.aggregate([{"$match":{"amenity":{"$exists":1}}},
                       {"$group":{"_id":"$amenity",
                                  "count":{"$sum":1}}},
                       {"$sort":{"count":-1}},
                       {"$limit":5}])
{ "_id" : "parking", "count" : 6774 }
{ "_id" : "bicycle_parking", "count" : 4868 }
{ "_id" : "school", "count" : 4693 }
{ "_id" : "place_of_worship", "count" : 4641 }
{ "_id" : "restaurant", "count" : 3154 }
</pre>

<p>Top 5 postcodes:</p>

<pre>&gt; db.NY_osm.aggregate([{"$match":{"addr.postcode":{"$exists":1}}},
                       {"$group":{"_id":"$addr.postcode",
                                  "count":{"$sum":1}}},
                       {"$sort":{"count":-1}},
                       {"$limit":5}])
{ "_id" : "10314", "count" : 23066 }
{ "_id" : "11234", "count" : 20139 }
{ "_id" : "10312", "count" : 17841 }
{ "_id" : "10306", "count" : 16186 }
{ "_id" : "11236", "count" : 15225 }
</pre>

<p>Top 5 cuisines:</p>

<pre>&gt; db.NY_osm.aggregate([{"$match":{"amenity":"restaurant",
                                  "cuisine":{"$exists":1}}},
                       {"$group":{"_id":"$cuisine",
                                  "count":{"$sum":1}}},
                       {"$sort":{"count":-1}},
                       {"$limit":5}])
{ "_id" : "italian", "count" : 221 }
{ "_id" : "american", "count" : 173 }
{ "_id" : "pizza", "count" : 163 }
{ "_id" : "mexican", "count" : 120 }
{ "_id" : "chinese", "count" : 98 }
</pre>
</article>
  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="hidden">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>


    </div>
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2016 <span title="0.08648s from github-fe130-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
      </button>
      You can't perform that action at this time.
    </div>


      
      <script crossorigin="anonymous" integrity="sha256-dOKIA1HONo2PClLxKnRStCK+9jl9VHfYEgIH6nnw39k=" src="https://assets-cdn.github.com/assets/frameworks-74e2880351ce368d8f0a52f12a7452b422bef6397d5477d8120207ea79f0dfd9.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-Vx67mEMB8a4oFYa6NOojslu0kkHLdlp+TG6FW0LtW1U=" src="https://assets-cdn.github.com/assets/github-571ebb984301f1ae281586ba34ea23b25bb49241cb765a7e4c6e855b42ed5b55.js"></script>
      
      
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"></path></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"></path></svg>
    </button>
  </div>
</div>

  </body>
</html>

